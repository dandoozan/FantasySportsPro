import _util as util
import _fanDuelCommon as fd

DATA_DIR = 'data'
OUTPUT_FILE = util.createFullPathFilename(DATA_DIR, 'data_2016.csv')
DATE_FORMAT = '%Y-%m-%d'
SEASON_START_DATE = util.getDate(2016, 10, 25)
ONE_DAY = util.getOneDay()
END_DATE = util.getDate(2016, 12, 20)# util.getYesterdayAsDate()

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
    'derrick jones jr.': ['derrick jones, jr.', 'derrick jones'],
    'timothe luwawu-cabarrot': 'timothe luwawu',
    'maurice ndour': 'maurice n\'dour',
    'wesley matthews': 'wes matthews',
    'john lucas iii': 'john lucas',
    'james ennis iii': 'james ennis',

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
    'r.j. hunter': 'rj hunter',

    #RotoGrinderStartingLineups
    'tim hardaway jr.': 'tim hardaway',

    #from createDataFile.py, investigate these
    #'amare stoudemire': 'amar\'e stoudemire',
    #'louis amundson': 'lou amundson',
    #'maurice williams': 'mo williams',
    #'chuck hayes': 'charles hayes',
}
TEAM_KNOWN_ALIASES = {
    'ATL': ['atl', 'atlanta hawks', 'atlanta'],
    'CHI': ['chi', 'chicago bulls', 'chicago'],
    'CLE': ['cle', 'cleveland cavaliers', 'cleveland'],
    'BOS': ['bos', 'boston celtics', 'boston'],
    'BKN': ['bkn', 'brooklyn nets', 'brooklyn'],
    'CHA': ['cha', 'charlotte hornets', 'charlotte'],
    'DAL': ['dal', 'dallas mavericks', 'dallas'],
    'DEN': ['den', 'denver nuggets', 'denver'],
    'DET': ['det', 'detroit pistons', 'detroit'],
    'GS': ['gsw', 'golden state warriors', 'golden state'],
    'HOU': ['hou', 'houston rockets', 'houston'],
    'IND': ['ind', 'indiana pacers', 'indiana'],
    'LAC': ['lac', 'los angeles clippers', 'la clippers', 'l.a. clippers'],
    'LAL': ['lal', 'los angeles lakers', 'l.a. lakers'],
    'MEM': ['mem', 'memphis grizzlies', 'memphis'],
    'MIA': ['mia', 'miami heat', 'miami'],
    'MIL': ['mil', 'milwaukee bucks', 'milwaukee'],
    'MIN': ['min', 'minnesota timberwolves', 'minnesota'],
    'NO': ['nop', 'new orleans pelicans', 'new orleans'],
    'NY': ['nyk', 'new york knicks', 'new york'],
    'OKC': ['okc', 'oklahoma city thunder', 'oklahoma city'],
    'ORL': ['orl', 'orlando magic', 'orlando'],
    'PHI': ['phi', 'philadelphia 76ers', 'philadelphia'],
    'PHO': ['pho', 'phoenix suns', 'phoenix'],
    'POR': ['por', 'portland trail blazers', 'portland'],
    'SAC': ['sac', 'sacramento kings', 'sacramento'],
    'SA': ['sas', 'san antonio spurs', 'san antonio'],
    'TOR': ['tor', 'toronto raptors', 'toronto'],
    'UTA': ['uta', 'utah jazz', 'utah'],
    'WAS': ['was', 'washington wizards', 'washington'],
}

PLAYERS_WHO_DID_NOT_PLAY_UP_TO = {
    '2016-10-26': {
        'aaron gordon',
        'al horford',
        'al jefferson',
        'alex abrines',
        'alex len',
        'alexis ajinca',
        'amir johnson',
        'andre drummond',
        'andre roberson',
        'andrew bogut',
        'andrew harrison',
        'andrew wiggins',
        'anthony davis',
        'anthony tolliver',
        'aron baynes',
        'arron afflalo',
        'avery bradley',
        'ben mclemore',
        'beno udrih',
        'boban marjanovic',
        'bojan bogdanovic',
        'brandon ingram',
        'brandon knight',
        'brandon rush',
        'brook lopez',
        'buddy hield',
        'c.j. miles',
        'chris mccullough',
        'clint capela',
        'cody zeller',
        'cole aldrich',
        'corey brewer',
        'cory joseph',
        'd\'angelo russell',
        'd.j. augustin',
        'danilo gallinari',
        'dante cunningham',
        'dario saric',
        'demar derozan',
        'demarcus cousins',
        'demarre carroll',
        'deron williams',
        'devin booker',
        'deyonta davis',
        'dion waiters',
        'dirk nowitzki',
        'domantas sabonis',
        'dorian finney-smith',
        'dragan bender',
        'dwight powell',
        'e\'twaun moore',
        'elfrid payton',
        'emmanuel mudiay',
        'enes kanter',
        'eric bledsoe',
        'eric gordon',
        'ersan ilyasova',
        'evan fournier',
        'garrett temple',
        'gerald green',
        'gerald henderson',
        'giannis antetokounmpo',
        'glenn robinson iii',
        'goran dragic',
        'gorgui dieng',
        'greg monroe',
        'greivis vasquez',
        'harrison barnes',
        'hassan whiteside',
        'henry ellenson',
        'hollis thompson',
        'isaiah thomas',
        'isaiah whitehead',
        'ish smith',
        'j.j. barea',
        'jabari parker',
        'jae crowder',
        'jahlil okafor',
        'jakob poeltl',
        'jamal murray',
        'jameer nelson',
        'james ennis',
        'james harden',
        'james johnson',
        'jamychal green',
        'jared dudley',
        'jason terry',
        'jaylen brown',
        'jeff green',
        'jeff teague',
        'jerami grant',
        'jeremy lamb',
        'jeremy lin',
        'joe harris',
        'joe young',
        'joel embiid',
        'john henson',
        'jon leuer',
        'jonas jerebko',
        'jonas valanciunas',
        'jordan clarkson',
        'juancho hernangomez',
        'julius randle',
        'justin anderson',
        'justin hamilton',
        'justise winslow',
        'jusuf nurkic',
        'k.j. mcdaniels',
        'karl-anthony towns',
        'kemba walker',
        'kenneth faried',
        'kentavious caldwell-pope',
        'kosta koufos',
        'kris dunn',
        'kyle lowry',
        'kyle singler',
        'lance stephenson',
        'langston galloway',
        'larry nance jr.',
        'lavoy allen',
        'leandro barbosa',
        'lou williams',
        'luis scola',
        'luke babbitt',
        'luol deng',
        'malachi richardson',
        'malcolm brogdon',
        'marc gasol',
        'marcelo huertas',
        'marco belinelli',
        'marcus morris',
        'mario hezonja',
        'marquese chriss',
        'marvin williams',
        'matt barnes',
        'matthew dellavedova',
        'metta world peace',
        'michael beasley',
        'michael gbinije',
        'michael kidd-gilchrist',
        'mike conley',
        'miles plumlee',
        'mirza teletovic',
        'monta ellis',
        'myles turner',
        'nemanja bjelica',
        'nene hilario',
        'nick young',
        'nicolas batum',
        'nicolas brussino',
        'nik stauskas',
        'nikola jokic',
        'nikola vucevic',
        'norman powell',
        'omer asik',
        'omri casspi',
        'p.j. tucker',
        'pascal siakam',
        'patrick patterson',
        'paul george',
        'quincy acy',
        'ramon sessions',
        'rashad vaughn',
        'richaun holmes',
        'ricky rubio',
        'robert covington',
        'rodney mcgruder',
        'rodney stuckey',
        'rondae hollis-jefferson',
        'roy hibbert',
        'rudy gay',
        'russell westbrook',
        'ryan anderson',
        'sam dekker',
        'sean kilpatrick',
        'semaj christon',
        'serge ibaka',
        'sergio rodriguez',
        'seth curry',
        'shabazz muhammad',
        'solomon hill',
        'spencer hawes',
        'stanley johnson',
        'steven adams',
        't.j. mcconnell',
        't.j. warren',
        'tarik black',
        'terrence jones',
        'terrence ross',
        'terry rozier',
        'thaddeus young',
        'tim frazier',
        'timofey mozgov',
        'timothe luwawu-cabarrot',
        'tobias harris',
        'trevor ariza',
        'trevor booker',
        'ty lawson',
        'tyler ennis',
        'tyler johnson',
        'tyler ulis',
        'tyler zeller',
        'tyson chandler',
        'victor oladipo',
        'vince carter',
        'wade baldwin iv',
        'wesley matthews',
        'will barton',
        'willie cauley-stein',
        'willie reed',
        'wilson chandler',
        'zach lavine',
        'zach randolph',
    },
    '2016-10-27': {
        'andrew nicholson',
        'austin rivers',
        'blake griffin',
        'bradley beal',
        'brandon bass',
        'chris paul',
        'cristiano felicio',
        'daniel ochefu',
        'deandre jordan',
        'deandre\' bembry',
        'dennis schroder',
        'diamond stone',
        'doug mcdermott',
        'dwight howard',
        'dwyane wade',
        'isaiah canaan',
        'j.j. redick',
        'jamal crawford',
        'jason smith',
        'jimmy butler',
        'john wall',
        'kelly oubre jr.',
        'kent bazemore',
        'kris humphries',
        'kyle korver',
        'luc richard mbah a moute',
        'malcolm delaney',
        'marcin gortat',
        'marcus thornton',
        'markieff morris',
        'marreese speights',
        'michael carter-williams',
        'mike muscala',
        'nikola mirotic',
        'otto porter',
        'paul millsap',
        'rajon rondo',
        'raymond felton',
        'robin lopez',
        'shabazz napier',
        'sheldon mcclellan',
        'taj gibson',
        'taurean prince',
        'thabo sefolosha',
        'tim hardaway jr.',
        'tomas satoransky',
        'trey burke',
        'walter tavares',
        'wesley johnson',
    },
    '2016-10-28': {
        'a.j. hammons',
        'bismack biyombo',
        'bobby brown',
        'c.j. watson',
        'c.j. wilcox',
        'darrun hilliard',
        'derrick favors',
        'georges niang',
        'joel bolomboy',
        'joffrey lauvergne',
        'kevin seraphin',
        'kyle wiltjer',
        'montrezl harrell',
        'raul neto',
        'salah mejri',
        'stephen zimmerman jr.',
        'thomas robinson',
    },
    '2016-10-29': {
        'anthony bennett',
        'bobby portis',
        'cheick diallo',
        'dejounte murray',
        'denzel valentine',
        'frank kaminsky',
        'jarell martin',
        'jordan mickey',
        'kay felder',
        'paul zipser',
        'rakeem christmas',
        'tony snell',
        'troy daniels',
        'troy williams',
    },
    '2016-10-30': {
        'anthony morrow',
        'jose calderon',
        'thon maker',
    },
    '2016-10-31': {
        'alan williams',
    },
    '2016-11-01': {
        'aaron brooks',
        'jake layman',
        'james michael mcadoo',
        'jordan hill',
        'maurice ndour',
        'pat connaughton',
        'tony allen',
        'tyus jones',
        'udonis haslem',
    },
    '2016-11-02': {
        'ivica zubac',
        'james young',
        'jerian grant',
        'marcus smart',
        'nick collison',
        'treveon graham',
    },
    '2016-11-03': {
        'darrell arthur',
    },
    '2016-11-04': {
        'alec burks',
        'brian roberts',
        'chandler parsons',
        'gordon hayward',
        'josh richardson',
    },
    '2016-11-05': {
        'adreian payne',
        'arinze onuaku',
        'gary harris',
        'georgios papagiannis',
        'john lucas iii',
        'jordan farmar',
        'malik beasley',
        'mike miller',
        'skal labissiere',
        'steve novak',
    },
    '2016-11-06': {
        'demetrius jackson',
        'lucas nogueira',
    },
    '2016-11-07': {
        'aaron harrison',
        'arinze onuaku',
        'brian roberts',
        'christian wood',
        'damjan rudez',
        'derrick williams',
    },
    '2016-11-08': {
        'darren collison',
        'jarnell stokes',
        'randy foye',
    },
    '2016-11-09': {
        'alan anderson',
        'danny green',
        'fred vanvleet',
        'kelly olynyk',
        'tim quarterman',
    },
    '2016-11-10': {},
    '2016-11-11': {
        'danuel house',
    },
    '2016-11-12': {
        'archie goodwin',
        'john jenkins',
        'josh mcroberts',
    },
    '2016-11-15': {
        'r.j. hunter',
    },
    '2016-11-16': {
        'alonzo gee',
    },
    '2016-11-17': {
        'patrick beverley',
    },
    '2016-11-18': {
        'jrue holiday',
        'paul pierce',
        'reggie bullock',
    },
    '2016-11-19': {
        'derrick jones jr.',
    },
    '2016-11-20': {
        'marshall plumlee',
    },
    '2016-11-21': {
        'jerryd bayless',
    },
    '2016-11-22': {
        'anthony brown',
    },
    '2016-11-26': {
        'ian mahinmi',
    },
    '2016-11-28': {
        'bruno caboclo',
        'wayne ellington',
    },
    '2016-11-30': {
        'devin harris',
        'mike scott',
    },
    '2016-12-04': {
        'reggie jackson',
    },
    '2016-12-10': {
        'reggie williams',
    },
    'never': {
        'louis amundson', #historical
        'joel anthony', #historical
        'markel brown', #historical
        'alec burks', #no games
        'tyreke evans', #no games
        'festus ezeli', #no games
        'patricio garino', #not on nba.com
        'john holland', #no games
        'jonathan holmes', #not on nba.com
        'josh huestis', #no games
        'damien inglis', #historical
        'livio jean-charles', #not on nba.com
        'cory jefferson', #historical
        'grant jerrett', #historical
        'brice johnson', #no games
        'chris johnson', #there are 2 chris johnsons, both historical
        'cameron jones', #not on nba.com
        'dahntay jones', #historical
        'damian jones', #no games
        'caris levert', #not on nba.com
        'nerlens noel', #no games
        'chinanu onuaku', #no games
        'phil pressey', #historical
        'chasson randle', #not on nba.com, only in 10/25 in fanduel
        'henry sims', #not on nba.com
        'tiago splitter', #no games
        'greg stiemsma', #not on nba.com
        'j.p. tokoto', #not on nba.com, only in 10/25 in fanduel
        'elliot williams', #not on nba.com, only in 10/25 in fanduel
        'brandan wright', #no games
    }
}

ROTOGRINDER_KNOWN_MISSING = {
    'cory jefferson', 'louis amundson', 'derrick favors', 'kevon looney', 'tim quarterman', 'alec burks', 'davis bertans', 'nicolas laprovittola', 'damien inglis', 'guillermo hernangomez', 'phil pressey', 'damian jones', 'raul neto', 'livio jean-charles', 'henry sims', 'dahntay jones', 'cameron jones', 'pat connaughton', 'chasson randle', 'grant jerrett', 'mindaugas kuzminskas', 'bryn forbes', 'joel bolomboy', 'maurice ndour', 'john holland',
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

    #2016-11-08
    'kyle korver',
    'larry nance jr.',

    'alex abrines',
    'richaun holmes',
    'archie goodwin',
    'yogi ferrell',
    'alonzo gee',

    #2016-11-21
    'jerryd bayless',

    #2016-11-23
    'anthony brown',

    #2016-11-25
    'ryan kelly',

    #2016-12-12
    'spencer dinwiddie',
}

TBX_MISSING_PLAYERS = {}

#------------ Misc ------------
def replaceUnicodeChars(string):
    return string.replace(u'\u00c1', 'A').replace(u'\u00e1', 'a').replace(u'\u00e9', 'e').replace(u'\u00ed', 'i').replace(u'\u00f3', 'o')
def joinFirstLastNames(obj, firstNameKey, lastNameKey):
    return ' '.join([getValue(obj, firstNameKey), getValue(obj, lastNameKey)])
def getNameValue(obj, key, prefix=''):
    return getValue(obj, key, prefix).lower()
def getValue(obj, key, prefix=''):
    value = obj[prefix + key]
    if util.isUnicode(value):
        return replaceUnicodeChars(value).strip()
    if util.isString(value):
        return value.strip()
    return value
def setValue(obj, key, newValue, prefix=''):
    obj[prefix + key] = newValue
def removePercentSigns(obj, keys, prefix):
    for key in keys:
        obj[prefix + key] = util.removePercentSign(getValue(obj, key, prefix))
def replaceAllOccurrences(obj, oldValue, newValue):
    for key in obj:
        if getValue(obj, key, '') == oldValue:
            setValue(obj, key, newValue)

#------------ Find File ------------
def findCsvFile(fullPathToDir, dateStr):
    return util.createFullPathFilename(fullPathToDir, util.createCsvFilename(dateStr))
def findJsonFile(fullPathToDir, dateStr):
    return util.createFullPathFilename(fullPathToDir, util.findLatestDatetimeFileForDate(fullPathToDir, dateStr))
def findNbaFile(fullPathToDir, dateStr):
    #get previous day's file
    usedDiffFile = False
    currDate = util.parseAsDate(dateStr)
    while currDate > SEASON_START_DATE:
        currDate = currDate - ONE_DAY
        fullPathFilename = util.createFullPathFilename(fullPathToDir, util.createJsonFilename(util.formatDate(currDate)))
        if util.fileExists(fullPathFilename):
            if usedDiffFile:
                util.headsUp('Used different file for date=' + dateStr + ', file used=' + fullPathFilename)
            return fullPathFilename
        usedDiffFile = True
    return None

#------------ Parse Row ------------
def parseFanDuelRow(row, dateStr, prefix):
    #add Name, which is a join of firstname and lastname
    setValue(row, 'Name', joinFirstLastNames(row, 'First Name', 'Last Name'))

    #add date to row
    setValue(row, 'Date', dateStr)

    #add IsHome
    setValue(row, 'Home', 'Home' if (getValue(row, 'Game').split('@')[1].strip() == getValue(row, 'Team')) else 'Away')

    #set '' to 'none' in injury cols
    #also lowercase the value if it's not ''
    injuryIndicator = getValue(row, 'InjuryIndicator')
    setValue(row, 'InjuryIndicator', 'none' if injuryIndicator == '' else injuryIndicator.lower())
    injuryDetails = getValue(row, 'InjuryDetails')
    setValue(row, 'InjuryDetails', 'none' if injuryDetails == '' else injuryDetails.lower())

    return getNameValue(row, 'Name'), row
def parseFanDuelJsonRow(row, dateStr, prefix):
    #'features': ['Date', 'Name','Position','FPPG','GamesPlayed','Salary','Home','Team','Opponent','InjuryIndicator','InjuryDetails'],

    #add Name, which is a join of firstname and lastname
    setValue(row, 'Name', joinFirstLastNames(row, 'first_name', 'last_name'))

    #add date to row
    setValue(row, 'Date', dateStr)

    #set nulls to 'None' in injury cols
    if getValue(row, 'InjuryIndicator') == None:
        setValue(row, 'InjuryIndicator', 'none')
    if getValue(row, 'InjuryDetails') == None:
        setValue(row, 'InjuryDetails', 'none')

    #set nulls to 0 in FPPG and GamesPlayed
    if getValue(row, 'FPPG') == None:
        setValue(row, 'FPPG', 0)
    if getValue(row, 'GamesPlayed') == None:
        setValue(row, 'GamesPlayed', 0)

    return getNameValue(row, 'Name'), row
def parseRotoGuruRow(row, dateStr, prefix):
    #convert to float just to make sure all values can be parsed to floats
    row['FantasyPoints'] = float(row['FantasyPoints'].strip())

    #set 'DNP' and 'NA' to 0 in Minutes
    minutes = getValue(row, 'Minutes')
    row['Minutes'] = 0. if (minutes == 'DNP' or minutes == 'NA') else float(minutes)

    #reverse name bc it's in format: 'lastname, firstname'
    playerName = row['Name'].strip().split(', ')
    playerName.reverse()
    playerName = ' '.join(playerName).lower()

    return playerName, row
def parseNumberFireRow(row, dateStr, prefix):
    return row['NF_Name'].strip().lower(), row
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

    #set nulls to 0s for 'line'
    row['RG_line'] = 0 if row['RG_line'] == None else int(row['RG_line'])

    #parse everything else to int/float to make sure
    #they're all in the right format
    intCols = ['RG_movement']
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
def parseRotoGrinderAdvancedPlayerStatsRow(row, dateStr, prefix):
    #check for Name == '&nbsp;', and if so return None
    if getValue(row, 'PLAYER', prefix) == '&nbsp;':
        return None, None

    #remove percent signs
    removePercentSigns(row, ['EFGPCT', 'TSPCT', 'USGPCT', 'POW_AST', 'POW_BLK', 'POW_PTS', 'POW_REB', 'POW_STL'], prefix)

    #replace all occurrences of '&nbsp' with 0
    replaceAllOccurrences(row, '&nbsp;', 0)

    util.mapSome(int, row, util.addPrefixToArray(['D_RT', 'O_RT'], prefix))
    util.mapSome(float, row, util.addPrefixToArray(['EFGPCT', 'TSPCT', 'USGPCT', 'POW_AST', 'POW_BLK', 'POW_PTS', 'POW_REB', 'POW_STL'], prefix))
    return getNameValue(row, 'PLAYER', prefix), row
def parseRotoGrinderMarketWatchRow(row, dateStr, prefix):
    newRow = {}
    #add all values to row
    sites = ['dd', 'dk', 'fa', 'fd', 'fdft', 'rstr', 'y']
    for site in sites:
        #handle y! differently because it has the exclamation
        siteObj = util.getObjValue(row, 'y!') if site == 'y' else util.getObjValue(row, site)
        if siteObj:
            change = int(siteObj['change'])
            current = int(siteObj['current'])
        else:
            change = 0
            current = 0
        setValue(newRow, site + '_change', change, prefix)
        setValue(newRow, site + '_current', current, prefix)
    return getNameValue(row, 'player'), newRow
def parseRotoGrinderOptimalLineupRow(row, dateStr, prefix):
    #set onteam to 1
    newRow = { prefix + 'OnTeam': 1 }
    return getNameValue(row, 'Player', prefix), newRow
def parseRotoGrinderDefenseVsPositionCheatSheetRow(row, dateStr, prefix):
    #convert each to int/float
    util.mapSome(int, row, util.addPrefixToArray([ 'CRK', 'SFRK', 'SGRK', 'PFRK', 'PGRK'], prefix))
    util.mapSome(float, row, util.addPrefixToArray(['CFPPG', 'SFFPPG', 'SGFPPG', 'PFFPPG', 'PGFPPG'], prefix))
    return row[prefix + 'TEAM'].strip().lower(), row
def parseRotoGrinderStartingLineupsRow(row, dateStr, prefix):
    name = row['data']['text'].strip()
    order = int(row['data']['order'].strip())
    isStarter = 1 if order <= 5 else 0

    #Im not sure what status is, but it might be important
    #I've seen it equal 'B' and 'C'
    #I think these are B=Best Guess and C=Confirmed
    status = row['data']['status'].strip()

    row = { 'Order': order, 'Starter': isStarter, 'Status': status, }

    return name.lower(), util.addPrefixToObj(row, prefix)
def parseRotoGrinderOffenseVsDefenseBasicRow(row, dateStr, prefix):
    #remove the '%' from FGPCT
    fgPct = row[prefix + 'FGPCT'].strip()
    row[prefix + 'FGPCT'] = fgPct[:-1] if fgPct[-1] == '%' else fgPct

    #make sure all values are floats
    util.mapSome(float, row, util.addPrefixToArray(['AST', 'STL', 'FGM', 'TO', '3PM', 'BLK', 'FGPCT', 'REB', 'PTS', 'FGA'], prefix))
    return row[prefix + 'OFFENSE'].strip().lower(), row
def parseRotoGrinderBackToBackRow(row, dateStr, prefix):
    #handle the later file format (it started on 11/4)
    if (prefix + 'Today Situation') in row:
        situation = getValue(row, 'Today Situation', prefix)
    else:
        situation = getValue(row, 'Situation', prefix)

    #set to 'None' if situation is blank
    if situation == '':
        situation = 'None'

    setValue(row, 'Situation', situation, prefix)

    return getNameValue(row, 'Team', prefix), row
def parseNbaRow(row, dateStr, prefix):
    return row[prefix + 'PLAYER_NAME'].strip().lower(), row
def parseNbaTeamRow(row, dateStr, prefix):
    return row[prefix + 'TEAM_NAME'].strip().lower(), row
#def parseRotoGrinderOffenseVsDefenseAdvancedRow(row, dateStr, prefix):
#    #make sure all values are floats
#    util.mapSome(float, row, util.addPrefixToArray(['OFFRTG', 'PPG', 'PPG-A', 'AVGRTG', 'DEFRTG', 'PACE', 'PTS'], prefix))
#    return row[prefix + 'OFFENSE'].strip().lower(), row

#------------ Handle Duplicates ------------
def handleRotoGrinderDuplicates(oldMatch, newMatch):
    oldMatchPoints = float(oldMatch['RG_points'])
    newMatchPoints = float(newMatch['RG_points'])
    if oldMatchPoints > 0 and newMatchPoints == 0:
        return oldMatch
    if newMatchPoints > 0 and oldMatchPoints == 0:
        return newMatch
    util.stop('In handleDuplicates for RotoGrinder, and dont know which to return')

#------------ Load File ------------
def loadCsvFile(fullPathFilename, keyRenameMap, prefix, delimiter):
    return util.loadCsvFile(fullPathFilename, keyRenameMap=keyRenameMap, delimiter=delimiter, prefix=prefix)
def loadJsonFile(fullPathFilename, keyRenameMap, prefix, delimiter):
    jsonData = util.loadJsonFile(fullPathFilename)

    for item in jsonData:
        #first, rename the keys
        if keyRenameMap:
            util.renameKeys(keyRenameMap, item)

        #then, add the prefix
        if prefix:
            util.addPrefixToObj(item, prefix)

    return jsonData
def loadFanDuelJsonFile(fullPathFilename, keyRenameMap, prefix, delimiter):
    #add home or away indicator to each player's obj
    jsonData = util.loadJsonFile(fullPathFilename)
    players = jsonData['players']
    fixtures = jsonData['fixtures']
    teams = jsonData['teams']
    for player in players:
        fixtureId = player['fixture']['_members'][0]
        teamId = player['team']['_members'][0]
        #find home and away teams
        for fixture in fixtures:
            if fixture['id'] == fixtureId:
                homeTeamId = fixture['home_team']['team']['_members'][0]
                awayTeamId = fixture['away_team']['team']['_members'][0]
                isHome = teamId == homeTeamId
                break
        #find team full name
        for team in teams:
            if team['id'] == teamId:
                teamName = team['code']
                break
        #find opponent team full name
        opponentTeamId = awayTeamId if isHome else homeTeamId
        for team in teams:
            if team['id'] == opponentTeamId:
                opponentTeamName = team['code']
                break

        #set team, opponent, and home
        player['Team'] = teamName.strip()
        player['Opponent'] = opponentTeamName.strip()
        player['Home'] = 'Home' if isHome else 'Away'

        util.renameKeys(keyRenameMap, player)

    return players
def loadNbaJsonFile(fullPathFilename, keyRenameMap, prefix, delimiter):
    rows = []
    jsonData = util.loadJsonFile(fullPathFilename)
    colNames = util.addPrefixToArray(jsonData['resultSets'][0]['headers'], prefix)
    rowData = jsonData['resultSets'][0]['rowSet']
    for row in rowData:
        rows.append(dict(zip(colNames, row)))
    return rows
def loadRotoGrinderStartingLineupsFile(fullPathFilename, keyRenameMap, prefix, delimiter):
    rows = []
    jsonData = util.loadJsonFile(fullPathFilename)
    matchups = jsonData.values()
    for matchup in matchups:
        teamHomePlayers = matchup['data']['team_home']['data']['lineups']['collection'].values()
        teamAwayPlayers = matchup['data']['team_away']['data']['lineups']['collection'].values()
        rows.extend(teamHomePlayers)
        rows.extend(teamAwayPlayers)
    return rows
def loadRotoGrinderMarketWatchFile(fullPathFilename, keyRenameMap, prefix, delimiter):
    jsonData = util.loadJsonFile(fullPathFilename)
    return jsonData.values()
def loadRotoGrinderOptimalLineupFile(fullPathFilename, keyRenameMap, prefix, delimiter):
    csvData = loadCsvFile(fullPathFilename, keyRenameMap, prefix, delimiter)
    #remove last row
    return csvData[:-1]

#------------ Common ------------
def loadDataFromFile(fullPathToDir, findFileFunction, loadFileFunction, parseRowFunction, handleDuplicates, features, dateStr, keyRenameMap={}, delimiter=',', prefix=''):
    data = {}

    fullPathFilename = findFileFunction(fullPathToDir, dateStr)
    print '    Loading file: %s...' % fullPathFilename

    if fullPathFilename and util.fileExists(fullPathFilename):
        rows = loadFileFunction(fullPathFilename, keyRenameMap, prefix, delimiter)
        for row in rows:
            playerName, playerData = parseRowFunction(row, dateStr, prefix)
            if playerName != None:
                if playerName in data:
                    if handleDuplicates:
                        util.headsUp('Found duplicate name: ' + playerName)
                        playerData = handleDuplicates(data[playerName], playerData)
                        if not playerData:
                            util.stop('Handle duplicates failed to give back new data')
                    else:
                        util.stop('Got a duplicate name and no handleDuplicates function, name=' + playerName)
                data[playerName] = util.filterObj(features, playerData)
    else:
        util.stop('File not found for date=' + dateStr)
        pass

    return data
def loadDataFromDir(fullPathToDir, findFileFunction, loadFileFunction, parseRowFunction, handleDuplicates, features, startDate, endDate, keyRenameMap={}, delimiter=',', prefix=''):
    print '    Loading dir:', fullPathToDir
    data = {}
    currDate = startDate
    while currDate <= endDate:
        currDateStr = util.formatDate(currDate)
        if currDateStr not in fd.DATES_WITH_NO_CONTESTS:
            data[currDateStr] = loadDataFromFile(fullPathToDir, findFileFunction, loadFileFunction, parseRowFunction, handleDuplicates, features, currDateStr, keyRenameMap, delimiter, prefix)
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
def findMatchingName(name, newData, isTeam):

    #first, check for exact match
    if hasExactMatch(name, newData):
        return name

    #then, check if it's a known mismatch name
    nameMap = TEAM_KNOWN_ALIASES if isTeam else KNOWN_ALIASES
    if name in nameMap:
        misMatchedName = nameMap[name]
        if isinstance(misMatchedName, list):
            for mmName in misMatchedName:
                if hasExactMatch(mmName, newData):
                    return mmName
        else:
            if hasExactMatch(misMatchedName, newData):
                return misMatchedName
    '''comment this out bc it makes the program run slow.  Uncomment if i need to automatically find mismatched names for new data
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
    #'''
    #if all fails return name, and let the parent handle it
    return name

def playerIsKnownToBeMissing(dateStr, name, knownMissingObj):
    return name in knownMissingObj or (dateStr in knownMissingObj and name in knownMissingObj[dateStr])
def playerDidNotPlayOnOrUpToDate(date, name):
    #first, check if they're in 'never'
    if name in PLAYERS_WHO_DID_NOT_PLAY_UP_TO['never']:
        return True

    #then, check each date starting with tomorrow up to the end
    currDate = date + ONE_DAY
    while currDate <= END_DATE:
        currDateStr = util.formatDate(currDate)
        if currDateStr in PLAYERS_WHO_DID_NOT_PLAY_UP_TO and name in PLAYERS_WHO_DID_NOT_PLAY_UP_TO[currDateStr]:
            return True
        currDate = currDate + ONE_DAY
    return False
def getTeam(playerData):
    return playerData['Team']
def getOppTeam(playerData):
    return playerData['Opponent']
def playerIsInData(data, name, isTeam):
    for dateStr in data:
        for nme in data[dateStr]:
            if nme == findMatchingName(name, data[dateStr], isTeam):
                return True
    return False

def mergeData(obj1, obj2, dataSourceName, isTeam, isOpp, ignoreMissingNames, knownMissingObj, containsY, usePrevDay, startDate, endDate):
    print 'Merging data...'
    dateStrs = obj1.keys()
    dateStrs.sort()
    for dateStr in dateStrs:
        if dateStr in obj2:
            for name in obj1[dateStr]:
                playerData = obj1[dateStr][name]
                if isTeam:
                    name = getOppTeam(playerData) if isOpp else getTeam(playerData)
                obj2Name = findMatchingName(name, obj2[dateStr], isTeam)
                if obj2Name in obj2[dateStr]:
                    playerData.update(obj2[dateStr][obj2Name])
                else: #name is missing from data
                    date = util.parseAsDate(dateStr)
                    if ignoreMissingNames \
                            or playerIsKnownToBeMissing(dateStr, name, knownMissingObj) \
                            or playerDidNotPlayOnOrUpToDate(date - ONE_DAY if usePrevDay else date, name) \
                            or playerIsInData(obj2, name, isTeam): #it's oh well in this case; at least i know it's not a name mismatch
                        #util.headsUp('Found known missing player, date=' + dateStr + ', name=' + name)
                        if containsY:
                            #set FantasyPoints to 0 for these people who are known to be missing
                            playerData.update({ 'FantasyPoints': 0, 'Minutes': 0 })
                    else:
                        #tbx
                        if dataSourceName not in TBX_MISSING_PLAYERS:
                            TBX_MISSING_PLAYERS[dataSourceName] = {}

                        if dateStr in TBX_MISSING_PLAYERS[dataSourceName]:
                            TBX_MISSING_PLAYERS[dataSourceName][dateStr].append(name)
                        else:
                            TBX_MISSING_PLAYERS[dataSourceName][dateStr] = [name]

                        util.headsUp('Name not found in obj2, date=' + dateStr + ', name=' + name)
        else:
            #stop if i'm expecting the date to be in obj2
            date = util.parseAsDate(dateStr)
            if date >= startDate and date <= endDate:
                util.stop('Date not found in obj2, date=' + dateStr)

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
        'name': 'FanDuel_fromPlayersManuallyDownloaded',
        'isBaseData': True,
        'endDate': util.getDate(2016, 11, 7),
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
        'name': 'FanDuel_fromPlayers',
        'isBaseData': True,
        'extendFeatures': False,
        'features': ['Date', 'Name','Position','FPPG','GamesPlayed','Salary','Home','Team','Opponent','InjuryIndicator','InjuryDetails'],
        'findFileFunction': findJsonFile,
        'fullPathToDir': util.joinDirs(DATA_DIR, 'rawDataFromFanDuel', 'Players'),
        'keyRenameMap': {
            'position': 'Position',
            'fppg': 'FPPG',
            'played': 'GamesPlayed',
            'salary': 'Salary',
            'injury_status': 'InjuryIndicator',
            'injury_details': 'InjuryDetails',
        },
        'loadFileFunction': loadFanDuelJsonFile,
        'parseRowFunction': parseFanDuelJsonRow,
        'startDate': util.getDate(2016, 11, 8),
    },
    {
        'name': 'RotoGuru',
        'containsY': True,
        'delimiter': ';',
        #'endDate': util.getYesterdayAsDate(),
        'features': ['FantasyPoints', 'Minutes'],
        'fullPathToDir': util.joinDirs(DATA_DIR, 'rawDataFromRotoGuru', '2016'),
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
            '2016-11-07': {
                'lance stephenson',
            },
            '2016-11-08': {
                'jordan farmar',
                'lance stephenson',
                'walter tavares',
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

            #2016-11-08
            'a.j. hammons',
            'jordan farmar',
            'lance stephenson',

            #2016-11-18
            'alonzo gee',

            #2016-11-23
            'anthony brown',

            #2016-12-13
            'reggie williams',
        },
        'parseRowFunction': parseNumberFireRow,
        'prefix': 'NF_',
    },
    {
        'name': 'RotoGrinderPlayerProjections',
        'handleDuplicates': handleRotoGrinderDuplicates,
        'features': [
            #15=DD, DraftDay
            #19=?
            #20=DK, DraftKings
            #28=fa, FantasyAces
            #43=FDraft (fdft), FantasyDraft
            #50=Y!, Yahoo
            #58=rstr, Rosters

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
        'findFileFunction': findJsonFile,
        'fullPathToDir': util.joinDirs(DATA_DIR, 'rawDataFromRotoGrinders', 'PlayerProjections'),
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
        'knownMissingObj': ROTOGRINDER_KNOWN_MISSING,
        'loadFileFunction': loadJsonFile,
        'parseRowFunction': parseRotoGrinderPlayerProjectionsRow,
        'prefix': 'RG_',
    },
    {
        'name': 'RotoGrinderAdvancedPlayerStats',
        'features': [
            'RG_ADV_D_RT',
            'RG_ADV_O_RT',
            'RG_ADV_POW_AST',
            'RG_ADV_POW_BLK',
            'RG_ADV_POW_PTS',
            'RG_ADV_POW_REB',
            'RG_ADV_POW_STL',
            'RG_ADV_EFGPCT',
            'RG_ADV_TSPCT',
            'RG_ADV_USGPCT',
        ],
        'findFileFunction': findJsonFile,
        'fullPathToDir': util.joinDirs(DATA_DIR, 'rawDataFromRotoGrinders', 'AdvancedPlayerStats'),
        'keyRenameMap': {
            'USG%': 'USGPCT',
            'TS%': 'TSPCT',
            'EFG%': 'EFGPCT',
            'D-RT': 'D_RT',
            'O-RT': 'O_RT',
            'POW-AST': 'POW_AST',
            'POW-BLK': 'POW_BLK',
            'POW-PTS': 'POW_PTS',
            'POW-REB': 'POW_REB',
            'POW-STL': 'POW_STL',
        },
        'knownMissingObj': ROTOGRINDER_KNOWN_MISSING,
        'loadFileFunction': loadJsonFile,
        'parseRowFunction': parseRotoGrinderAdvancedPlayerStatsRow,
        'prefix': 'RG_ADV_',
        'startDate': util.getDate(2016, 10, 26),
    },
    {
        'name': 'RotoGrinderStartingLineups',
        'features': [
            'RG_START_Order',
            'RG_START_Starter',
            'RG_START_Status',
        ],
        'findFileFunction': findJsonFile,
        'fullPathToDir': util.joinDirs(DATA_DIR, 'rawDataFromRotoGrinders', 'StartingLineups'),
        'knownMissingObj': {
            '2016-10-29': { 'rakeem christmas' },
            '2016-11-01': { 'rakeem christmas' },
            '2016-11-03': { 'rakeem christmas' },
            '2016-11-05': { 'rakeem christmas', 'georgios papagiannis' },
            '2016-11-06': { 'georgios papagiannis' },
            '2016-11-07': { 'rakeem christmas' },
            '2016-11-08': { 'georgios papagiannis' },
            '2016-11-09': { 'rakeem christmas' },
            '2016-11-10': { 'georgios papagiannis' },
            '2016-11-11': { 'rakeem christmas', 'georgios papagiannis' },
            '2016-11-12': { 'rakeem christmas' },
            '2016-11-14': { 'rakeem christmas' },
            '2016-11-16': { 'rakeem christmas', 'georgios papagiannis' },
            '2016-11-18': { 'rakeem christmas', 'georgios papagiannis' },
            '2016-11-20': { 'rakeem christmas' },
            '2016-11-21': { 'rakeem christmas' },
            '2016-11-23': { 'rakeem christmas' },
        },
        'loadFileFunction': loadRotoGrinderStartingLineupsFile,
        'parseRowFunction': parseRotoGrinderStartingLineupsRow,
        'prefix': 'RG_START_',
        'startDate': util.getDate(2016, 10, 26),
    },
    {
        'name': 'RotoGrinderMarketWatch',
        'features': [
            'RG_MW_dk_current',
            'RG_MW_dk_change',
            'RG_MW_fa_current',
            'RG_MW_fa_change',
            'RG_MW_y_current',
            'RG_MW_y_change',
            'RG_MW_dd_current',
            'RG_MW_dd_change',
            'RG_MW_rstr_current',
            'RG_MW_rstr_change',
            #'RG_MW_fd_current', #<-- same as 'Salary'
            'RG_MW_fd_change',
            'RG_MW_fdft_current',
            'RG_MW_fdft_change',
        ],
        'findFileFunction': findJsonFile,
        'fullPathToDir': util.joinDirs(DATA_DIR, 'rawDataFromRotoGrinders', 'MarketWatch'),
        'knownMissingObj': ROTOGRINDER_KNOWN_MISSING,
        'loadFileFunction': loadRotoGrinderMarketWatchFile,
        'parseRowFunction': parseRotoGrinderMarketWatchRow,
        'prefix': 'RG_MW_',
        'startDate': util.getDate(2016, 10, 26),
    },
    {
        'name': 'RotoGrinderOptimalTeam',
        'features': [ 'RG_OL_OnTeam' ],
        'fullPathToDir': util.joinDirs(DATA_DIR, 'rawDataFromRotoGrinders', 'OptimalLineup'),
        'ignoreMissingNames': True,
        'loadFileFunction': loadRotoGrinderOptimalLineupFile,
        'parseRowFunction': parseRotoGrinderOptimalLineupRow,
        'prefix': 'RG_OL_',
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
        'findFileFunction': findJsonFile,
        'fullPathToDir': util.joinDirs(DATA_DIR, 'rawDataFromRotoGrinders', 'DefenseVsPositionCheatSheet'),
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
        'loadFileFunction': loadJsonFile,
        'parseRowFunction': parseRotoGrinderDefenseVsPositionCheatSheetRow,
        'prefix': 'RG_OPP_DVP_',
        'startDate': util.getDate(2016, 10, 26),
    },
    {
        'name': 'RotoGrinderOffenseVsDefenseBasic',
        'features': [
            'RG_OVD_AST',
            'RG_OVD_STL',
            'RG_OVD_FGM',
            'RG_OVD_TO',
            'RG_OVD_3PM',
            'RG_OVD_BLK',
            'RG_OVD_FGPCT',
            'RG_OVD_REB',
            'RG_OVD_PTS',
            'RG_OVD_FGA',
        ],
        'findFileFunction': findJsonFile,
        'fullPathToDir': util.joinDirs(DATA_DIR, 'rawDataFromRotoGrinders', 'OffenseVsDefenseBasic'),
        'isTeam': True,
        'keyRenameMap': {
            'FG%': 'FGPCT',
        },
        'loadFileFunction': loadJsonFile,
        'parseRowFunction': parseRotoGrinderOffenseVsDefenseBasicRow,
        'prefix': 'RG_OVD_',
        'startDate': util.getDate(2016, 10, 26),
    },
    {
        'name': 'RotoGrinderOffenseVsDefenseBasicOpponent',
        'features': [
            'RG_OVD_OPP_AST',
            'RG_OVD_OPP_STL',
            'RG_OVD_OPP_FGM',
            'RG_OVD_OPP_TO',
            'RG_OVD_OPP_3PM',
            'RG_OVD_OPP_BLK',
            'RG_OVD_OPP_FGPCT',
            'RG_OVD_OPP_REB',
            'RG_OVD_OPP_PTS',
            'RG_OVD_OPP_FGA',
        ],
        'findFileFunction': findJsonFile,
        'fullPathToDir': util.joinDirs(DATA_DIR, 'rawDataFromRotoGrinders', 'OffenseVsDefenseBasic'),
        'isOpp': True,
        'isTeam': True,
        'keyRenameMap': {
            'FG%': 'FGPCT',
        },
        'loadFileFunction': loadJsonFile,
        'parseRowFunction': parseRotoGrinderOffenseVsDefenseBasicRow,
        'prefix': 'RG_OVD_OPP_',
        'startDate': util.getDate(2016, 10, 26),
    },
    {
        'name': 'RotoGrinderBackToBack',
        'features': [ 'RG_B2B_Situation' ],
        'fullPathToDir': util.joinDirs(DATA_DIR, 'rawDataFromRotoGrinders', 'BackToBack'),
        'isTeam': True,
        'parseRowFunction': parseRotoGrinderBackToBackRow,
        'prefix': 'RG_B2B_',
    },
    {
        'name': 'RotoGrinderBackToBackOpponent',
        'features': [ 'RG_B2B_OPP_Situation' ],
        'fullPathToDir': util.joinDirs(DATA_DIR, 'rawDataFromRotoGrinders', 'BackToBack'),
        'isOpp': True,
        'isTeam': True,
        'parseRowFunction': parseRotoGrinderBackToBackRow,
        'prefix': 'RG_B2B_OPP_',
    },
    {
        'name': 'NBASeasonPlayerTraditional',
        'features': [
            'NBA_S_P_TRAD_GP',
            'NBA_S_P_TRAD_W',
            'NBA_S_P_TRAD_L',
            'NBA_S_P_TRAD_W_PCT',
            'NBA_S_P_TRAD_MIN',
            'NBA_S_P_TRAD_FGM',
            'NBA_S_P_TRAD_FGA',
            'NBA_S_P_TRAD_FG_PCT',
            'NBA_S_P_TRAD_FG3M',
            'NBA_S_P_TRAD_FG3A',
            'NBA_S_P_TRAD_FG3_PCT',
            'NBA_S_P_TRAD_FTM',
            'NBA_S_P_TRAD_FTA',
            'NBA_S_P_TRAD_FT_PCT',
            'NBA_S_P_TRAD_OREB',
            'NBA_S_P_TRAD_DREB',
            'NBA_S_P_TRAD_REB',
            'NBA_S_P_TRAD_AST',
            'NBA_S_P_TRAD_TOV',
            'NBA_S_P_TRAD_STL',
            'NBA_S_P_TRAD_BLK',
            'NBA_S_P_TRAD_BLKA',
            'NBA_S_P_TRAD_PF',
            'NBA_S_P_TRAD_PFD',
            'NBA_S_P_TRAD_PTS',
            'NBA_S_P_TRAD_PLUS_MINUS',
            'NBA_S_P_TRAD_DD2',
            'NBA_S_P_TRAD_TD3',
        ],
        'findFileFunction': findNbaFile,
        'fullPathToDir': util.joinDirs(DATA_DIR, 'rawDataFromStatsNba', 'Season', 'Traditional', '2016'),
        'loadFileFunction': loadNbaJsonFile,
        'parseRowFunction': parseNbaRow,
        'prefix': 'NBA_S_P_TRAD_',
        'usePrevDay': True,
    },
    {
        'name': 'NBASeasonPlayerAdvanced',
        'features': [
            'NBA_S_P_ADV_OFF_RATING',
            'NBA_S_P_ADV_DEF_RATING',
            'NBA_S_P_ADV_NET_RATING',
            'NBA_S_P_ADV_AST_PCT',
            'NBA_S_P_ADV_AST_TO',
            'NBA_S_P_ADV_AST_RATIO',
            'NBA_S_P_ADV_OREB_PCT',
            'NBA_S_P_ADV_DREB_PCT',
            'NBA_S_P_ADV_REB_PCT',
            'NBA_S_P_ADV_TM_TOV_PCT',
            'NBA_S_P_ADV_EFG_PCT',
            'NBA_S_P_ADV_TS_PCT',
            'NBA_S_P_ADV_USG_PCT',
            'NBA_S_P_ADV_PACE',
            'NBA_S_P_ADV_PIE',
            'NBA_S_P_ADV_FGM_PG',
            'NBA_S_P_ADV_FGA_PG',
        ],
        'findFileFunction': findNbaFile,
        'fullPathToDir': util.joinDirs(DATA_DIR, 'rawDataFromStatsNba', 'Season', 'Advanced', '2016'),
        'loadFileFunction': loadNbaJsonFile,
        'parseRowFunction': parseNbaRow,
        'prefix': 'NBA_S_P_ADV_',
        'usePrevDay': True,
    },
    {
        'name': 'NBASeasonPlayerDefense',
        'features': [
            'NBA_S_P_DEF_DEF_RATING',
            'NBA_S_P_DEF_PCT_DREB',
            'NBA_S_P_DEF_PCT_STL',
            'NBA_S_P_DEF_PCT_BLK',
            'NBA_S_P_DEF_OPP_PTS_OFF_TOV',
            'NBA_S_P_DEF_OPP_PTS_2ND_CHANCE',
            'NBA_S_P_DEF_OPP_PTS_FB',
            'NBA_S_P_DEF_OPP_PTS_PAINT',
            'NBA_S_P_DEF_DEF_WS',
        ],
        'findFileFunction': findNbaFile,
        'fullPathToDir': util.joinDirs(DATA_DIR, 'rawDataFromStatsNba', 'Season', 'Defense', '2016'),
        'loadFileFunction': loadNbaJsonFile,
        'parseRowFunction': parseNbaRow,
        'prefix': 'NBA_S_P_DEF_',
        'usePrevDay': True,
    },
    {
        'name': 'NBAPlayerBios',
        'features': [
            'NBA_PB_AGE',
            'NBA_PB_PLAYER_HEIGHT_INCHES',
            'NBA_PB_PLAYER_WEIGHT',
            'NBA_PB_COLLEGE',
            'NBA_PB_COUNTRY',
            'NBA_PB_DRAFT_YEAR',
            'NBA_PB_DRAFT_ROUND',
            'NBA_PB_DRAFT_NUMBER',
        ],
        'findFileFunction': findJsonFile,
        'fullPathToDir': util.joinDirs(DATA_DIR, 'rawDataFromStatsNba', 'Season', 'PlayerBios', '2016'),
        'knownMissingObj': {
            '2016-12-04': {
                'reggie jackson',
            },
        },
        'loadFileFunction': loadNbaJsonFile,
        'parseRowFunction': parseNbaRow,
        'prefix': 'NBA_PB_',
    },
    {
        'name': 'NBADailyPlayerTraditional',
        'features': [
            'NBA_TODAY_GP', #maybe remove this bc it will always be 1
            'NBA_TODAY_W',
            'NBA_TODAY_L',
            'NBA_TODAY_W_PCT',
            'NBA_TODAY_MIN',
            'NBA_TODAY_FGM',
            'NBA_TODAY_FGA',
            'NBA_TODAY_FG_PCT',
            'NBA_TODAY_FG3M',
            'NBA_TODAY_FG3A',
            'NBA_TODAY_FG3_PCT',
            'NBA_TODAY_FTM',
            'NBA_TODAY_FTA',
            'NBA_TODAY_FT_PCT',
            'NBA_TODAY_OREB',
            'NBA_TODAY_DREB',
            'NBA_TODAY_REB',
            'NBA_TODAY_AST',
            'NBA_TODAY_TOV',
            'NBA_TODAY_STL',
            'NBA_TODAY_BLK',
            'NBA_TODAY_BLKA',
            'NBA_TODAY_PF',
            'NBA_TODAY_PFD',
            'NBA_TODAY_PTS',
            'NBA_TODAY_PLUS_MINUS',
            'NBA_TODAY_DD2',
            'NBA_TODAY_TD3',
        ],
        'findFileFunction': findJsonFile,
        'fullPathToDir': util.joinDirs(DATA_DIR, 'rawDataFromStatsNba', 'Daily', 'Traditional', '2016'),
        'loadFileFunction': loadNbaJsonFile,
        'parseRowFunction': parseNbaRow,
        'prefix': 'NBA_TODAY_',
    },
    {
        'name': 'NBASeasonTeamTraditional',
        'features': [
            'NBA_S_T_TRAD_GP',
            'NBA_S_T_TRAD_W',
            'NBA_S_T_TRAD_L',
            'NBA_S_T_TRAD_W_PCT',
            'NBA_S_T_TRAD_MIN',
            'NBA_S_T_TRAD_FGM',
            'NBA_S_T_TRAD_FGA',
            'NBA_S_T_TRAD_FG_PCT',
            'NBA_S_T_TRAD_FG3M',
            'NBA_S_T_TRAD_FG3A',
            'NBA_S_T_TRAD_FG3_PCT',
            'NBA_S_T_TRAD_FTM',
            'NBA_S_T_TRAD_FTA',
            'NBA_S_T_TRAD_FT_PCT',
            'NBA_S_T_TRAD_OREB',
            'NBA_S_T_TRAD_DREB',
            'NBA_S_T_TRAD_REB',
            'NBA_S_T_TRAD_AST',
            'NBA_S_T_TRAD_TOV',
            'NBA_S_T_TRAD_STL',
            'NBA_S_T_TRAD_BLK',
            'NBA_S_T_TRAD_BLKA',
            'NBA_S_T_TRAD_PF',
            'NBA_S_T_TRAD_PFD',
            'NBA_S_T_TRAD_PTS',
            'NBA_S_T_TRAD_PLUS_MINUS',
        ],
        'findFileFunction': findNbaFile,
        'fullPathToDir': util.joinDirs(DATA_DIR, 'rawDataFromStatsNba', 'Season', 'Team_Traditional', '2016'),
        'isTeam': True,
        'loadFileFunction': loadNbaJsonFile,
        'parseRowFunction': parseNbaTeamRow,
        'prefix': 'NBA_S_T_TRAD_',
        'usePrevDay': True,
    },
    {
        'name': 'NBASeasonTeamOpponentTraditional',
        'features': [
            'NBA_S_OPPT_TRAD_GP',
            'NBA_S_OPPT_TRAD_W',
            'NBA_S_OPPT_TRAD_L',
            'NBA_S_OPPT_TRAD_W_PCT',
            'NBA_S_OPPT_TRAD_MIN',
            'NBA_S_OPPT_TRAD_FGM',
            'NBA_S_OPPT_TRAD_FGA',
            'NBA_S_OPPT_TRAD_FG_PCT',
            'NBA_S_OPPT_TRAD_FG3M',
            'NBA_S_OPPT_TRAD_FG3A',
            'NBA_S_OPPT_TRAD_FG3_PCT',
            'NBA_S_OPPT_TRAD_FTM',
            'NBA_S_OPPT_TRAD_FTA',
            'NBA_S_OPPT_TRAD_FT_PCT',
            'NBA_S_OPPT_TRAD_OREB',
            'NBA_S_OPPT_TRAD_DREB',
            'NBA_S_OPPT_TRAD_REB',
            'NBA_S_OPPT_TRAD_AST',
            'NBA_S_OPPT_TRAD_TOV',
            'NBA_S_OPPT_TRAD_STL',
            'NBA_S_OPPT_TRAD_BLK',
            'NBA_S_OPPT_TRAD_BLKA',
            'NBA_S_OPPT_TRAD_PF',
            'NBA_S_OPPT_TRAD_PFD',
            'NBA_S_OPPT_TRAD_PTS',
            'NBA_S_OPPT_TRAD_PLUS_MINUS',
        ],
        'findFileFunction': findNbaFile,
        'fullPathToDir': util.joinDirs(DATA_DIR, 'rawDataFromStatsNba', 'Season', 'Team_Traditional', '2016'),
        'isOpp': True,
        'isTeam': True,
        'loadFileFunction': loadNbaJsonFile,
        'parseRowFunction': parseNbaTeamRow,
        'prefix': 'NBA_S_OPPT_TRAD_',
        'usePrevDay': True,
    },

    #{
    #    'name': 'RotoGrinderOffenseVsDefenseAdvanced',
    #    'features': [
    #        'RG_OVD_ADV_OFFRTG',
    #        'RG_OVD_ADV_PPG',
    #        'RG_OVD_ADV_PPG-A',
    #        'RG_OVD_ADV_AVGRTG',
    #        'RG_OVD_ADV_DEFRTG',
    #        'RG_OVD_ADV_PACE',
    #        'RG_OVD_ADV_PTS',
    #    ],
    #    'findFileFunction': findJsonFile,
    #    'fullPathToDir': util.joinDirs(DATA_DIR, 'rawDataFromRotoGrinders', 'OffenseVsDefenseAdvanced'),
    #    'isTeam': True,
    #    'loadFileFunction': loadJsonFile,
    #    'parseRowFunction': parseRotoGrinderOffenseVsDefenseAdvancedRow,
    #    'prefix': 'RG_OVD_ADV_',
    #},


    #{
    #    'name': '',
    #    'features': [],
    #    'fullPathToDir': util.joinDirs(DATA_DIR, ''),
    #    'parseRowFunction': ,
    #},
]
'''
#tbx
DATA_SOURCES = [
    {
        'name': 'FanDuel_fromPlayersManuallyDownloaded',
        'isBaseData': True,
        'endDate': util.getDate(2016, 11, 7),
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
        'name': 'FanDuel_fromPlayers',
        'isBaseData': True,
        'extendFeatures': False,
        'features': ['Date', 'Name','Position','FPPG','GamesPlayed','Salary','Home','Team','Opponent','InjuryIndicator','InjuryDetails'],
        'findFileFunction': findJsonFile,
        'fullPathToDir': util.joinDirs(DATA_DIR, 'rawDataFromFanDuel', 'Players'),
        'keyRenameMap': {
            'position': 'Position',
            'fppg': 'FPPG',
            'played': 'GamesPlayed',
            'salary': 'Salary',
            'injury_status': 'InjuryIndicator',
            'injury_details': 'InjuryDetails',
        },
        'loadFileFunction': loadFanDuelJsonFile,
        'parseRowFunction': parseFanDuelJsonRow,
        'startDate': util.getDate(2016, 11, 8),
    },
    {
        'name': 'RotoGuru',
        'containsY': True,
        'delimiter': ';',
        'endDate': util.getYesterdayAsDate(),
        'features': ['FantasyPoints'],
        'fullPathToDir': util.joinDirs(DATA_DIR, 'rawDataFromRotoGuru', '2016'),
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
            '2016-11-07': {
                'lance stephenson',
            },
            '2016-11-08': {
                'jordan farmar',
                'lance stephenson',
                'walter tavares',
            },
        },
        'parseRowFunction': parseRotoGuruRow,
    },
    {
        'name': 'RotoGrinderOptimalTeam',
        'features': [ 'RG_OL_OnTeam' ],
        'fullPathToDir': util.joinDirs(DATA_DIR, 'rawDataFromRotoGrinders', 'OptimalLineup'),
        'ignoreMissingNames': True,
        'loadFileFunction': loadRotoGrinderOptimalLineupFile,
        'parseRowFunction': parseRotoGrinderOptimalLineupRow,
        'prefix': 'RG_OL_',
    },

]
'''

#load fanduel data
data = {}

for dataSource in DATA_SOURCES:
    name = dataSource['name']
    print 'Loading data for %s...' % dataSource['name']

    containsY = util.getObjValue(dataSource, 'containsY', False)
    delimiter = util.getObjValue(dataSource, 'delimiter', ',')
    extendFeatures = util.getObjValue(dataSource, 'extendFeatures', True)
    features = dataSource['features']
    findFileFunction = util.getObjValue(dataSource, 'findFileFunction', findCsvFile)
    fullPathToDir = dataSource['fullPathToDir']
    handleDuplicates = util.getObjValue(dataSource, 'handleDuplicates', None)
    ignoreMissingNames = util.getObjValue(dataSource, 'ignoreMissingNames', False)
    isBaseData = util.getObjValue(dataSource, 'isBaseData', False)
    isOpp = util.getObjValue(dataSource, 'isOpp', False)
    isTeam = util.getObjValue(dataSource, 'isTeam', False)
    keyRenameMap = util.getObjValue(dataSource, 'keyRenameMap', {})
    knownMissingObj = util.getObjValue(dataSource, 'knownMissingObj', {})
    loadFileFunction = util.getObjValue(dataSource, 'loadFileFunction', loadCsvFile)
    parseRowFunction = dataSource['parseRowFunction']
    prefix = util.getObjValue(dataSource, 'prefix', '')
    usePrevDay = util.getObjValue(dataSource, 'usePrevDay', False)
    startDate = util.getObjValue(dataSource, 'startDate', (SEASON_START_DATE + ONE_DAY) if usePrevDay else SEASON_START_DATE)
    endDate = util.getObjValue(dataSource, 'endDate', END_DATE)

    newData = loadDataFromDir(fullPathToDir, findFileFunction, loadFileFunction, parseRowFunction, handleDuplicates, features, startDate, endDate, keyRenameMap, delimiter, prefix)

    if extendFeatures:
        X_NAMES.extend(features)

    if isBaseData:
        data.update(newData)
    else:
        mergeData(data, newData, name, isTeam, isOpp, ignoreMissingNames, knownMissingObj, containsY, usePrevDay, startDate, endDate)

if len(TBX_MISSING_PLAYERS) == 0:
    writeData(OUTPUT_FILE, data)
else:
    print '\nNot writing data because missing players were found:'
    dataSourceNames = TBX_MISSING_PLAYERS.keys()
    dataSourceNames.sort()
    for dataSourceName in dataSourceNames:
        print ' '
        print dataSourceName
        dateStrs = TBX_MISSING_PLAYERS[dataSourceName].keys()
        dateStrs.sort()
        for dateStr in dateStrs:
            print dateStr
            TBX_MISSING_PLAYERS[dataSourceName][dateStr].sort()
            for name in TBX_MISSING_PLAYERS[dataSourceName][dateStr]:
                print '\'' + name + '\','
