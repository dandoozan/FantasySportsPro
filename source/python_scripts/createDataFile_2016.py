from datetime import datetime, timedelta
import scraper
import _util as util

DATA_DIR = 'data'
OUTPUT_FILE = util.createFullPathFilename(DATA_DIR, 'data_2016.csv')
DATE_FORMAT = '%Y-%m-%d'
SEASON_START_DATE = datetime(2016, 10, 25)
ONE_DAY = timedelta(1)
END_DATE = datetime(2016, 11, 6)

Y_NAME = 'FantasyPoints'
X_NAMES = []

KNOWN_ALIASES = {
    'maurice harkless': 'moe harkless',
    'james michael mcadoo': 'james mcadoo',
    'lou williams': 'louis williams',
    'joe young': 'joseph young',
    'juancho hernangomez': 'juan hernangomez',
    'cristiano felicio': 'cristiano da silva felicio',
    'deandre\' bembry': 'deandre bembry',
    'wade baldwin iv': 'wade baldwin',
    'larry nance jr.': 'larry nance',
    'stephen zimmerman jr.': 'stephen zimmerman',
    'glenn robinson iii': 'glenn robinson',
    'kelly oubre jr.': 'kelly oubre',
    'patty mills': 'patrick mills',
    'j.j. barea': ['jose juan barea', 'jose barea'],
    'ish smith': 'ishmael smith',
    'luc richard mbah a moute': 'luc mbah a moute',
    'derrick jones jr.': 'derrick jones',
    'timothe luwawu-cabarrot': 'timothe luwawu',
    'maurice ndour': 'maurice n\'dour',
    'wesley matthews': 'wes matthews',
    'john lucas iii': 'john lucas',

    #nba
    'nene hilario': 'nene',
    'walter tavares': 'edy tavares',
    'guillermo hernangomez': 'willy hernangomez',
    'j.r. smith': 'jr smith',
    'c.j. mccollum': 'cj mccollum',
    'c.j. miles': 'cj miles',
    't.j. warren': 'tj warren',
    'p.j. tucker': 'pj tucker',
    'k.j. mcdaniels': 'kj mcdaniels',
    't.j. mcconnell': 'tj mcconnell',
    'j.j. redick': 'jj redick',
    'a.j. hammons': 'aj hammons',
    'c.j. wilcox': 'cj wilcox',
    'c.j. watson': 'cj watson',
}

TBX_MISSING_PLAYERS = {}

def parseFanDuelRow(row, dateStr, prefix):
    #add Name, which is a join of firstname and lastname
    row['Name'] = ' '.join([row['First Name'], row['Last Name']])

    #add date to row
    row['Date'] = dateStr

    #add IsHome
    row['Home'] = 'Home' if (row['Game'].split('@')[1] == row['Team']) else 'Away'

    #set '' to 'None' in injury cols
    if row['InjuryIndicator'] == '':
        row['InjuryIndicator'] = 'None'
    if row['InjuryDetails'] == '':
        row['InjuryDetails'] = 'None'

    playerName = row['Name'].lower()
    return playerName, row
def parseRotoGuruRow(row, dateStr, prefix):
    #convert to float just to make sure all values can be parsed to floats
    row['FantasyPoints'] = float(row['FantasyPoints'])

    #reverse name bc it's in format: 'lastname, firstname'
    playerName = row['Name'].split(', ')
    playerName.reverse()
    playerName = ' '.join(playerName).lower()

    return playerName, row
def parseNumberFireRow(row, dateStr, prefix):
    return row['NF_Name'].lower(), row
def parseRotoGrinderPlayerProjectionsRow(row, dateStr, prefix):
    #handle pownpct
    #remove the '%' from pownpct (eg. '25.00%' -> 25.00)
    #set to 0 if pownpct is null
    row['RG_pownpct'] = float(row['RG_pownpct'][:-1]) if (row['RG_pownpct'] and row['RG_pownpct'][-1] == '%') else 0.

    #handle deviation, ceil, and floor
    #first, set deviation to 0 if it is null
    if row['RG_deviation'] == None:
        #also verify that ceil and lower both equal null here
        if row['RG_ceil'] != None or row['RG_floor'] != None:
            util.stop('deviation is null, but ceil or floor are not.')
        row['RG_deviation'] = 0.
    else:
        row['RG_deviation'] = float(row['RG_deviation'])
    #now, for ceil and floor, set them to +/- devation if
    #they are null (there are more of these nulls than deviation nulls)
    row['RG_ceil'] = (float(row['RG_points']) + row['RG_deviation']) if row['RG_ceil'] == None else float(row['RG_ceil'])
    row['RG_floor'] = (float(row['RG_points']) - row['RG_deviation']) if row['RG_floor'] == None else float(row['RG_floor'])

    #handle saldiff and rankdiff
    #set salarydiff and rankdiff to 0 if they are null for now, but manually compute
    #it in the future when i get DK salary and rank
    row['RG_saldiff'] = 0 if row['RG_saldiff'] == None else int(row['RG_saldiff'])
    row['RG_rankdiff'] = 0 if row['RG_rankdiff'] == None else int(row['RG_rankdiff'])

    #parse everything else to int/float to make sure
    #they're all in the right format
    intCols = ['RG_line', 'RG_movement']
    floatCols = ['RG_overunder', 'RG_points', 'RG_ppdk',
        'RG_total', 'RG_contr', 'RG_minutes',
        'RG_points15', 'RG_points19', 'RG_points20',
        'RG_points28', 'RG_points43',
        'RG_points50', 'RG_points51', 'RG_points58']
    util.mapSome(int, row, intCols)
    util.mapSome(float, row, floatCols)

    #now, add the extra data under salaries obj (which is other sites' salary, rank info)
    salaries = row['RG_schedule']['data']['salaries']['collection']
    for salaryObj in salaries:
        dataObj = salaryObj['data']
        siteId = str(int(dataObj['site_id']))

        if siteId == '2': #fanduel
            row['RG_rank'] = int(dataObj['rank'])
        elif siteId == '20': #draftkings i think
            row['RG_rank20'] = int(dataObj['rank'])
            row['RG_rank_diff20'] = int(dataObj['rank_diff'])
            row['RG_salary20'] = float(dataObj['salary'])
            row['RG_diff20'] = int(dataObj['diff'])
        else:
            row['RG_salary' + siteId] = float(dataObj['salary'])
    return row['RG_player_name'].strip().lower(), row
def parseRotoGrinderDefenseVsPositionCheatSheetRow(row, dateStr, prefix):
    #convert each to int/float
    util.mapSome(int, row, util.addPrefixToArray([ 'CRK', 'SFRK', 'SGRK', 'PFRK', 'PGRK'], prefix))
    util.mapSome(float, row, util.addPrefixToArray(['CFPPG', 'SFFPPG', 'SGFPPG', 'PFFPPG', 'PGFPPG'], prefix))
    return row[prefix + 'TEAM'].strip(), row
def parseNbaRow(row, dateStr, prefix):
    intCols = util.addPrefixToArray([
        'W',
        'L',
        'DD2',
        'TD3',
    ], prefix)
    floatCols = util.addPrefixToArray([
        'AGE',
        'W_PCT',
        'MIN',
        'FGM',
        'FGA',
        'FG_PCT',
        'FG3M',
        'FG3A',
        'FG3_PCT',
        'FTM',
        'FTA',
        'FT_PCT',
        'OREB',
        'DREB',
        'REB',
        'AST',
        'TOV',
        'STL',
        'BLK',
        'BLKA',
        'PF',
        'PFD',
        'PTS',
        'PLUS_MINUS',
    ], prefix)

    #convert each to int/float
    util.mapSome(int, row, intCols)
    util.mapSome(float, row, floatCols)

    return row[prefix + 'PLAYER_NAME'].lower(), row

def handleRotoGrinderDuplicates(oldMatch, newMatch):
    oldMatchPoints = float(oldMatch['RG_points'])
    newMatchPoints = float(newMatch['RG_points'])
    if oldMatchPoints > 0 and newMatchPoints == 0:
        return oldMatch
    if newMatchPoints > 0 and oldMatchPoints == 0:
        return newMatch
    util.stop('In handleDuplicates for RotoGrinder, and dont know which to return')

def loadCsvFile(fullPathFilename, keyRenameMap, prefix, delimiter):
    return util.loadCsvFile(fullPathFilename, keyRenameMap=keyRenameMap, delimiter=delimiter, prefix=prefix)
def loadJsonFile(fullPathFilename, keyRenameMap, prefix, delimiter):
    jsonData = util.loadJsonFile(fullPathFilename)

    #append prefix to all keys
    for item in jsonData:
        #first, rename the keys
        if keyRenameMap:
            util.renameKeys(keyRenameMap, item)

        #then, add the prefix
        if prefix:
            util.addPrefixToObj(item, prefix)

    return jsonData
def loadNbaJsonFile(fullPathFilename, keyRenameMap, prefix, delimiter):
    rows = []
    jsonData = util.loadJsonFile(fullPathFilename)
    colNames = util.addPrefixToArray(jsonData['resultSets'][0]['headers'], prefix)
    rowData = jsonData['resultSets'][0]['rowSet']
    for row in rowData:
        rows.append(dict(zip(colNames, row)))
    return rows

def loadDataFromFile(fullPathToDir, loadFileFunction, parseRowFunction, handleDuplicates, features, dateStr, isJson, keyRenameMap={}, delimiter=',', prefix=''):
    data = {}

    filename = util.createJsonFilename(dateStr) if isJson else util.createCsvFilename(dateStr)
    print '    Loading file: %s...' % filename

    fullPathFilename = util.createFullPathFilename(fullPathToDir, filename)
    if util.fileExists(fullPathFilename):
        rows = loadFileFunction(fullPathFilename, keyRenameMap, prefix, delimiter)
        for row in rows:
            playerName, playerData = parseRowFunction(row, dateStr, prefix)
            if playerName in data:
                if handleDuplicates:
                    util.headsUp('Found duplicate name: ' + playerName)
                    newPlayerData = handleDuplicates(data[playerName], playerData)
                    if newPlayerData:
                        data[playerName] = newPlayerData
                    else:
                        util.stop('Handle duplicates failed to give back new data')
                else:
                    util.stop('Got a duplicate name: ' + playerName)
            #if fullPathFilename == 'data/rawDataFromRotoGrinders/PlayerProjections/2016-10-26.json':
            #    print playerData
            data[playerName] = util.filterObj(features, playerData)
    else:
        #util.headsUp('File not found: ' + fullPathFilename)
        pass

    return data
def loadDataFromDir(fullPathToDir, loadFileFunction, parseRowFunction, handleDuplicates, features, isJson, keyRenameMap={}, delimiter=',', prefix=''):
    print '    Loading dir:', fullPathToDir
    data = {}
    currDate = SEASON_START_DATE
    while currDate <= END_DATE:
        currDateStr = util.formatDate(currDate)
        dateData = loadDataFromFile(fullPathToDir, loadFileFunction, parseRowFunction, handleDuplicates, features, currDateStr, isJson, keyRenameMap, delimiter, prefix)
        if dateData:
            data[currDateStr] = dateData
        else:
            #util.headsUp('Data not found for date=' + currDateStr)
            pass
        currDate = currDate + ONE_DAY

    return data

def hasExactMatch(key, obj):
    return key in obj
def removePeriods(name):
    return name.replace('.', '')
def removeSuffix(name):
    validSuffices = { 'jr.', 'iv', 'iii' }
    nameSp = name.split(' ')
    if nameSp[-1] in validSuffices:
        return ' '.join(nameSp[:-1])
    return name
def findAllPlayersThatMatchFunction(name, newData, func):
    playerMatches = []

    newName = func(name)
    if newName and hasExactMatch(newName, newData):
        return [newName]

    for newDataName in newData:
        newName = func(newDataName)
        if newName == name:
            playerMatches.append(newName)

    return playerMatches
def findAllPlayerMatches(name, newData):
    playerMatches = []
    playerMatches.extend(findAllPlayersThatMatchFunction(name, newData, removePeriods))
    playerMatches.extend(findAllPlayersThatMatchFunction(name, newData, removeSuffix))
    return playerMatches
def findMatchingName(name, newData, nameMap={}):

    #first, check for exact match
    if hasExactMatch(name, newData):
        return name

    #then, check if it's a known mismatch name
    if name in nameMap:
        misMatchedName = nameMap[name]
        if isinstance(misMatchedName, list):
            for mmName in misMatchedName:
                if hasExactMatch(mmName, newData):
                    return mmName
        else:
            if hasExactMatch(misMatchedName, newData):
                return misMatchedName

    #then, check all permutations of the name and its reverse
    #print 'No match found for player=', name, ', searching for similar names...'
    playerMatches = findAllPlayerMatches(name, newData)
    numPlayerMatches = len(playerMatches)
    if numPlayerMatches > 1:
        util.stop('Multiple matches found for name=' + name + ', matches=' + ','.join(playerMatches))

    if numPlayerMatches == 1:
        newName = playerMatches[0]
        print '    Found different name: %s -> %s' % (name, newName)
        #add it to the known mismatches
        nameMap[name] = newName
        return newName
    return None
def playerIsKnownToBeMissing(dateStr, name, knownMissingObj):
    return (dateStr in knownMissingObj and name in knownMissingObj[dateStr]) or name in knownMissingObj
def getTeam(playerData):
    return playerData['Team']
def getOppTeam(playerData):
    return playerData['Opponent']
def mergeData(obj1, obj2, isTeam, isOpp, nameMap, knownMissingObj, containsY):
    print 'Merging data...'
    dateStrs = obj1.keys()
    dateStrs.sort()
    for dateStr in dateStrs:
        if dateStr in obj2:
            for name in obj1[dateStr]:
                playerData = obj1[dateStr][name]
                if isTeam:
                    name = getOppTeam(playerData) if isOpp else getTeam(playerData)
                obj2Name = findMatchingName(name, obj2[dateStr], nameMap)
                if obj2Name and obj2Name in obj2[dateStr]:
                    playerData.update(obj2[dateStr][obj2Name])
                else:
                    if not playerIsKnownToBeMissing(dateStr, name, knownMissingObj):
                        #tbx
                        if dateStr in TBX_MISSING_PLAYERS:
                            TBX_MISSING_PLAYERS[dateStr].append(name)
                        else:
                            TBX_MISSING_PLAYERS[dateStr] = [name]

                        util.headsUp('Name not found in obj2, date=' + dateStr + ', name=' + name)
                    else:
                        #util.headsUp('Found known missing player, date=' + dateStr + ', name=' + name)
                        if containsY:
                            #set FantasyPoints to 0 for these people who are known to be missing
                            playerData.update({ 'FantasyPoints': 0 })

        else:
            util.headsUp('Date not found in obj2, date=' + dateStr)

def writeData(fullPathFilename, data):
    colNames = [Y_NAME]
    colNames.extend(filter(lambda x: x != Y_NAME, X_NAMES))
    dataArr = []

    dateStrs = data.keys()
    dateStrs.sort() #sort by date
    for dateStr in dateStrs:
        names = data[dateStr].keys()
        names.sort() #sort by name
        for name in names:
            dataArr.append(data[dateStr][name])

    util.writeCsvFile(colNames, dataArr, fullPathFilename)

#============= MAIN =============

DATA_SOURCES = [
    {
        'name': 'FanDuel',
        'features': ['Date', 'Name','Position','FPPG','GamesPlayed','Salary','Home','Team','Opponent','InjuryIndicator','InjuryDetails'],
        'fullPathToDir': util.joinDirs(DATA_DIR, 'rawDataFromFanDuel', 'Players_manuallyDownloaded'),
        'keyRenameMap': {
            'Played': 'GamesPlayed',
            'Injury Indicator': 'InjuryIndicator',
            'Injury Details': 'InjuryDetails',
        },
        'parseRowFunction': parseFanDuelRow,
    },
    {
        'name': 'RotoGuru',
        'containsY': True,
        'delimiter': ';',
        'features': ['FantasyPoints'],
        'fullPathToDir': util.joinDirs(DATA_DIR, 'rawDataFromRotoGuru'),
        'keyRenameMap': { 'FD Pts': 'FantasyPoints' },
        'knownMissingObj': {
            '2016-10-25': {
                'cory jefferson', #he didn't play according to stats.nba.com
                'louis amundson', #he didn't play according to stats.nba.com
                'damien inglis', #he didn't play according to stats.nba.com
                'phil pressey', #he didn't play according to stats.nba.com
                'greg stiemsma', #he didn't play according to stats.nba.com
                'patricio garino', #this guy isn't even on nba.com
                'chasson randle', #this guy isn't even on nba.com
                'j.p. tokoto', #this guy isn't even on nba.com
                'livio jean-charles', #this guy isn't even on nba.com
                'markel brown', #he didn't play according to stats.nba.com
                'joel anthony', #he didn't play according to stats.nba.com
                'grant jerrett', #he didn't play according to stats.nba.com
                'henry sims', #he didn't play according to stats.nba.com
                'chris johnson', #he didn't play according to stats.nba.com
                'dahntay jones', #he didn't play according to stats.nba.com
                'elliot williams', #he didn't play according to stats.nba.com
                'john holland', #he didn't play according to stats.nba.com
                'cameron jones', #this guy isn't even on nba.com
                'jonathan holmes', #this guy isn't even on nba.com
            },'2016-10-31': {
                'taurean prince', #he didn't play according to stats.nba.com
                'walter tavares', #he didn't play according to stats.nba.com
            },
            '2016-11-01': {
                'jerami grant', #he didn't play according to stats.nba.com
            },
            '2016-11-02': {
                'taurean prince', #he actually did play, but only for 2 min and didn't accumulate any stats
                'walter tavares', #he didn't play according to stats.nba.com
            },
            '2016-11-04': {
                'taurean prince', #he didn't play according to stats.nba.com
                'walter tavares', #he didn't play according to stats.nba.com
                'joel bolomboy', #he didn't play according to stats.nba.com
            },
            '2016-11-05': {
                'taurean prince', #he actually did play, but only for 2 min and didn't accumulate any stats
                'walter tavares', #he didn't play according to stats.nba.com
            },
        },
        'parseRowFunction': parseRotoGuruRow,
    },
    {
        'name': 'NumberFire',
        'features': ['NF_Min', 'NF_Pts', 'NF_Reb', 'NF_Ast', 'NF_Stl', 'NF_Blk', 'NF_TO', 'NF_FP'],
        'fullPathToDir': util.joinDirs(DATA_DIR, 'rawDataFromNumberFire'),
        'knownMissingObj': {
            'cory jefferson', #he didn't play according to stats.nba.com
            'tim quarterman', #he didn't play according to stats.nba.com
            'davis bertans',
            'nicolas laprovittola',
            'damien inglis',
            'phil pressey',
            'deandre liggins',
            'cameron jones',
            'chasson randle',
            'grant jerrett',
            'ron baker',
            'mindaugas kuzminskas',
            'bryn forbes',
            'john holland',
            'j.p. tokoto',
            'jonathan holmes',
            'marshall plumlee',
            'patricio garino',
            'greg stiemsma',
            'rodney mcgruder',
            'metta world peace',
            'georgios papagiannis',
            'josh huestis',
            'kevin seraphin',
            'nerlens noel',
            'nicolas brussino',
            'timothe luwawu-cabarrot',
            'derrick jones jr.',
            'chris mccullough',
            'treveon graham',
            'chinanu onuaku',
            'demetrius jackson',
            'troy williams',
            'john jenkins',
            'john lucas iii',
            'bobby brown',
            'michael gbinije',
            'rakeem christmas',
            'beno udrih',
            'kyle wiltjer',
            'fred vanvleet',
            'dorian finney-smith',
            'sheldon mcclellan',
            'daniel ochefu',
            'walter tavares',
            'paul zipser',
            'dejounte murray',
            'danuel house',
            'darren collison',
            'r.j. hunter',
            'alec burks',
            'jeremy lamb',
            'mike scott',
            'bismack biyombo',
            'frank kaminsky',
            'michael carter-williams',
        },
        'parseRowFunction': parseNumberFireRow,
        'prefix': 'NF_',
    },
    {
        'name': 'RotoGrinderPlayerProjections',
        'handleDuplicates': handleRotoGrinderDuplicates,
        'features': [
            #Projection
            'RG_ceil',
            'RG_floor',
            'RG_points',
            'RG_ppdk',

            #Vegas Lines
            'RG_line', #chance that this player's team will win, lower number = higher chance
            'RG_movement', #diff between current 'total' and original 'total' when the vegas line opened (this changes by the minute/hour)
            'RG_overunder', #total points scored in the game
            'RG_total', #total points scored by player's team

            #Premium
            #'RG_rank', #rank at fanduel #always null
            'RG_contr', #contrarian rating (projected points / pown%)
            'RG_pownpct', #projected ownership percentage in large field tournaments

            #FD vs DK
            'RG_rankdiff', #diff between FD and DK rank (FD - DK)
            'RG_saldiff', #diff between FD and DK salaries (FD - DK)

            #Other
            'RG_deviation', #i suspect this is stdev of score, but im not sure
            'RG_minutes', #? im not sure if this is projected minutes or actual average or something else

            #inside schedule -> salaries obj
            'RG_rank', #fanduel
            'RG_salary15',
            'RG_salary19',
            'RG_rank20', 'RG_diff20', 'RG_rank_diff20', 'RG_salary20',
            'RG_salary28',
            'RG_salary43',
            'RG_salary50',
            #'RG_salary51', #no salary51 for some reason
            'RG_salary58',

            #projected points from other sites
            #'RG_points2', #fanduel (same as 'points')
            'RG_points15',
            'RG_points19',
            'RG_points20', #draftkings?
            'RG_points28',
            'RG_points43',
            'RG_points50',
            'RG_points51',
            'RG_points58',
        ],
        'fullPathToDir': util.joinDirs(DATA_DIR, 'rawDataFromRotoGrinders', 'PlayerProjections'),
        'isJson': True,
        'keyRenameMap': {
            'pown%': 'pownpct',
            'pt/$/k': 'ppdk',
            'o/u': 'overunder',
            '15': 'points15',
            '19': 'points19',
            '20': 'points20',
            '28': 'points28',
            '43': 'points43',
            '50': 'points50',
            '51': 'points51',
            '58': 'points58',
        },
        'knownMissingObj': {
            'cory jefferson',
            'louis amundson',
            'derrick favors',
            'kevon looney',
            'tim quarterman',
            'alec burks',
            'davis bertans',
            'nicolas laprovittola',
            'damien inglis',
            'guillermo hernangomez',
            'phil pressey',
            'damian jones',
            'raul neto',
            'livio jean-charles',
            'henry sims',
            'dahntay jones',
            'cameron jones',
            'pat connaughton',
            'chasson randle',
            'grant jerrett',
            'mindaugas kuzminskas',
            'bryn forbes',
            'joel bolomboy',
            'maurice ndour',
            'john holland',
            'jake layman', 'javale mcgee', 'j.p. tokoto', 'joel anthony', 'shabazz napier', 'danny green', 'dejounte murray', 'jonathan holmes', 'marshall plumlee', 'patricio garino', 'elliot williams', 'greg stiemsma', 'markel brown', 'kay felder', 'festus ezeli', 'chris johnson',
            'skal labissiere', 'brian roberts', 'adreian payne', 'tony allen', 'brandan wright', 'darrell arthur', 'nick collison', 'sam dekker', 'jarell martin', 'georges niang', 'tyus jones',
            'lucas nogueira', 'bismack biyombo', 'caris levert', 'thon maker', 'georgios papagiannis', 'josh huestis', 'christian wood', 'henry ellenson', 'udonis haslem', 'wayne ellington', 'mike miller', 'josh mcroberts', 'kevin seraphin', 'jose calderon',
            'nerlens noel', 'ivica zubac', 'a.j. hammons', 'timothe luwawu-cabarrot', 'isaiah whitehead', 'devin harris', 'derrick jones jr.', 'josh richardson', 'malachi richardson', 'steve novak', 'quincy acy', 'jordan mickey', 'patrick beverley', 'treveon graham', 'malik beasley', 'chinanu onuaku', 'arinze onuaku', 'demetrius jackson', 'jordan hill', 'james young', 'john jenkins', 'anthony bennett', 'john lucas iii', 'bruno caboclo', 'bobby brown', 'chandler parsons', 'marcus smart', 'kelly olynyk', 'gary harris', 'michael gbinije', 'alan williams', 'jrue holiday', 'randy foye', 'rakeem christmas', 'darrun hilliard', 'dragan bender', 'kyle wiltjer', 'jakob poeltl', 'frank kaminsky', 'fred vanvleet', 'boban marjanovic',
            'jarnell stokes',
            'dorian finney-smith', 'aaron harrison', 'tony snell', 'cheick diallo',
            'roy hibbert', 'james michael mcadoo', 'lance stephenson', 'paul zipser', 'jeremy lamb', 'sheldon mcclellan', 'damjan rudez', 'michael carter-williams', 'alan anderson', 'anderson varejao', 'brice johnson', 'paul pierce', 'reggie bullock', 'rodney stuckey', 'stephen zimmerman jr.', 'daniel ochefu', 'c.j. wilcox', 'patrick mccaw', 'george hill', 'diamond stone',
            'danuel house', 'derrick williams', 'r.j. hunter', 'boris diaw',
            'anthony tolliver', 'darren collison', 'metta world peace', 'will barton', 'deron williams', 'leandro barbosa', 'nicolas brussino', 'jae crowder', 'marcelo huertas', 'gerald green', 'al horford', 'miles plumlee', 'thomas robinson', 'dirk nowitzki', 'michael beasley',
            'tiago splitter', 'cole aldrich', 'ricky rubio', 'rudy gay', 'chris andersen', 'deandre\' bembry', 'jordan farmar', 'mike scott', 'tony parker', 'anthony morrow', 'john wall', 'jerian grant', 'walter tavares', 'taurean prince', 'james jones',
            'sasha vujacic', 'troy williams', 'chris mccullough', 'greivis vasquez', 'dante cunningham', 'tomas satoransky', 'jeremy lin', 'troy daniels', 'gordon hayward',
            'omri casspi', 'jordan mcrae', 'juancho hernangomez',
            'joel embiid', 'brandon bass', 'ron baker', 'jerami grant', 'timofey mozgov', 'nene hilario',
            'john henson', 'channing frye', 'c.j. watson', 'jeff withey', 'jahlil okafor', 'deyonta davis',
            'bobby portis',
            'jason terry', 'lamarcus aldridge', 'montrezl harrell', 'salah mejri',
            'denzel valentine', 'glenn robinson iii', 'brook lopez', 'rashad vaughn', 'cristiano felicio',
            'aaron brooks', 'joffrey lauvergne',
        },
        'parseRowFunction': parseRotoGrinderPlayerProjectionsRow,
        'prefix': 'RG_',
    },
    {
        'name': 'RotoGrinderDefenseVsPositionCheatSheet',
        'features': [
            'RG_OPP_DVP_CFPPG',
            'RG_OPP_DVP_CRK',
            'RG_OPP_DVP_PFFPPG',
            'RG_OPP_DVP_PFRK',
            'RG_OPP_DVP_PGFPPG',
            'RG_OPP_DVP_PGRK',
            'RG_OPP_DVP_SFFPPG',
            'RG_OPP_DVP_SFRK',
            'RG_OPP_DVP_SGFPPG',
            'RG_OPP_DVP_SGRK',
        ],
        'fullPathToDir': util.joinDirs(DATA_DIR, 'rawDataFromRotoGrinders', 'DefenseVsPositionCheatSheet'),
        'isJson': True,
        'isOpp': True,
        'isTeam': True,
        'keyRenameMap': {
            'C FPPG': 'CFPPG',
            'C RK': 'CRK',
            'PF FPPG': 'PFFPPG',
            'PF RK': 'PFRK',
            'PG FPPG': 'PGFPPG',
            'PG RK': 'PGRK',
            'SF FPPG': 'SFFPPG',
            'SF RK': 'SFRK',
            'SG FPPG': 'SGFPPG',
            'SG RK': 'SGRK'
        },
        'nameMap': {
            'ATL': 'Atlanta Hawks',
            'CHI': 'Chicago Bulls',
            'CLE': 'Cleveland Cavaliers',
            'BOS': 'Boston Celtics',
            'BKN': 'Brooklyn Nets',
            'CHA': 'Charlotte Hornets',
            'DAL': 'Dallas Mavericks',
            'DEN': 'Denver Nuggets',
            'DET': 'Detroit Pistons',
            'GS': 'Golden State Warriors',
            'HOU': 'Houston Rockets',
            'IND': 'Indiana Pacers',
            'LAC': 'Los Angeles Clippers',
            'LAL': 'Los Angeles Lakers',
            'MEM': 'Memphis Grizzlies',
            'MIA': 'Miami Heat',
            'MIL': 'Milwaukee Bucks',
            'MIN': 'Minnesota Timberwolves',
            'NO': 'New Orleans Pelicans',
            'NY': 'New York Knicks',
            'OKC': 'Oklahoma City Thunder',
            'ORL': 'Orlando Magic',
            'PHI': 'Philadelphia 76ers',
            'PHO': 'Phoenix Suns',
            'POR': 'Portland Trail Blazers',
            'SAC': 'Sacramento Kings',
            'SA': 'San Antonio Spurs',
            'TOR': 'Toronto Raptors',
            'UTA': 'Utah Jazz',
            'WAS': 'Washington Wizards',
        },
        'parseRowFunction': parseRotoGrinderDefenseVsPositionCheatSheetRow,
        'prefix': 'RG_OPP_DVP_',
    },
    {
        'name': 'NBA',
        'features': [
            'NBA_SEASON_AGE',
            'NBA_SEASON_W',
            'NBA_SEASON_L',
            'NBA_SEASON_W_PCT',
            'NBA_SEASON_MIN',
            'NBA_SEASON_FGM',
            'NBA_SEASON_FGA',
            'NBA_SEASON_FG_PCT',
            'NBA_SEASON_FG3M',
            'NBA_SEASON_FG3A',
            'NBA_SEASON_FG3_PCT',
            'NBA_SEASON_FTM',
            'NBA_SEASON_FTA',
            'NBA_SEASON_FT_PCT',
            'NBA_SEASON_OREB',
            'NBA_SEASON_DREB',
            'NBA_SEASON_REB',
            'NBA_SEASON_AST',
            'NBA_SEASON_TOV',
            'NBA_SEASON_STL',
            'NBA_SEASON_BLK',
            'NBA_SEASON_BLKA',
            'NBA_SEASON_PF',
            'NBA_SEASON_PFD',
            'NBA_SEASON_PTS',
            'NBA_SEASON_PLUS_MINUS',
            'NBA_SEASON_DD2',
            'NBA_SEASON_TD3',
        ],
        'fullPathToDir': util.joinDirs(DATA_DIR, 'rawDataFromStatsNba', 'Season', 'Traditional', '2016'),
        'isJson': True,
        'knownMissingObj': {
            #2016-11-06
            'darren collison',
            'devin harris',
            'derrick jones jr.',
            'john jenkins',
            'bruno caboclo',
            'kelly olynyk',
            'fred vanvleet',
            'jarnell stokes',

            #2016-11-05
            'brice johnson', 'tiago splitter', 'damjan rudez', 'alan anderson', 'nerlens noel', 'paul pierce', 'patrick beverley', 'mike scott', 'chinanu onuaku', 'arinze onuaku', 'josh huestis',
            'reggie bullock', 'r.j. hunter', 'danny green', 'danuel house',

            #2016-11-04
            'brandan wright', 'tim quarterman', 'alec burks', 'lucas nogueira', 'christian wood',
            'damian jones', 'wayne ellington', 'derrick williams', 'chandler parsons', 'josh mcroberts', 'jrue holiday', 'randy foye', 'brian roberts', 'marshall plumlee', 'gordon hayward', 'festus ezeli', 'aaron harrison', 'caris levert',

            #2016-11-03
            'malik beasley', 'skal labissiere', 'adreian payne', 'georgios papagiannis', 'gary harris', 'steve novak', 'demetrius jackson', 'john lucas iii', 'mike miller',

            #2016-11-01
            'josh richardson', 'ivica zubac',

            #2016-10-31
            'darrell arthur', 'jerian grant',

            #2016-10-30
            'tony allen', 'james michael mcadoo', 'nick collison', 'udonis haslem', 'alan williams',

            #2016-10-29
            'jordan hill', 'treveon graham', 'aaron brooks', 'pat connaughton', 'tyus jones', 'james young', 'maurice ndour', 'marcus smart', 'jake layman', 'thon maker',

            #2016-10-28
            'anthony morrow', 'jose calderon', 'kay felder', 'raul neto', 'anthony bennett', 'joel bolomboy', 'rakeem christmas', 'frank kaminsky', 'cheick diallo',

            #2016-10-27
            'denzel valentine', 'brandon bass', 'jordan mickey', 'walter tavares', 'bobby portis', 'paul zipser', 'dejounte murray', 'diamond stone',

            #2016-10-26
            'jarell martin', 'georges niang', 'bismack biyombo', 'kevin seraphin', 'a.j. hammons', 'timothe luwawu-cabarrot', 'stephen zimmerman jr.', 'montrezl harrell', 'troy williams', 'troy daniels', 'c.j. wilcox', 'bobby brown', 'thomas robinson', 'c.j. watson', 'darrun hilliard', 'kyle wiltjer', 'joffrey lauvergne', 'salah mejri', 'tony snell',

            #2016-10-25
            'cory jefferson', 'louis amundson', 'derrick favors', 'damien inglis', 'phil pressey', 'livio jean-charles', 'henry sims', 'dahntay jones', 'cameron jones', 'chasson randle', 'grant jerrett', 'john holland', 'j.p. tokoto', 'joel anthony', 'shabazz napier', 'jonathan holmes', 'patricio garino', 'elliot williams', 'greg stiemsma', 'markel brown', 'chris johnson',
        },
        'loadFileFunction': loadNbaJsonFile,
        'parseRowFunction': parseNbaRow,
        'prefix': 'NBA_SEASON_',
    },
    #{
    #    'name': '',
    #    'features': [],
    #    'fullPathToDir': util.joinDirs(DATA_DIR, ''),
    #    'parseRowFunction': ,
    #},
]


#load fanduel data
data = None

for dataSource in DATA_SOURCES:
    print 'Loading data for %s...' % dataSource['name']

    containsY = util.getObjValue(dataSource, 'containsY', False)
    delimiter = util.getObjValue(dataSource, 'delimiter', ',')
    features = dataSource['features']
    fullPathToDir = dataSource['fullPathToDir']
    handleDuplicates = util.getObjValue(dataSource, 'handleDuplicates', None)
    isJson = util.getObjValue(dataSource, 'isJson', False)
    isOpp = util.getObjValue(dataSource, 'isOpp', False)
    isTeam = util.getObjValue(dataSource, 'isTeam', False)
    keyRenameMap = util.getObjValue(dataSource, 'keyRenameMap', {})
    knownMissingObj = util.getObjValue(dataSource, 'knownMissingObj', {})
    loadFileFunction = util.getObjValue(dataSource, 'loadFileFunction', (loadJsonFile if isJson else loadCsvFile))
    nameMap = util.getObjValue(dataSource, 'nameMap', KNOWN_ALIASES)
    parseRowFunction = dataSource['parseRowFunction']
    prefix = util.getObjValue(dataSource, 'prefix', '')

    newData = loadDataFromDir(fullPathToDir, loadFileFunction, parseRowFunction, handleDuplicates, features, isJson, keyRenameMap, delimiter, prefix)
    X_NAMES.extend(features)

    if data == None:
        data = newData
    else:
        mergeData(data, newData, isTeam, isOpp, nameMap, knownMissingObj, containsY)

writeData(OUTPUT_FILE, data)

print 'Missing players:'
util.printObj(TBX_MISSING_PLAYERS)
