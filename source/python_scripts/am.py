import sys
import _util as util

PYTHON_SOURCE_DIR = util.joinDirs('source', 'python_scripts')

xAuthToken = util.readInput('Enter X-Auth-Token: ')
filesToRun = [
    #{ 'baseFilename': 'downloadFanDuelJson', 'args': [xAuthToken] },
    { 'baseFilename': 'scrapeFanDuel', 'args': [xAuthToken] },
    { 'baseFilename': 'downloadFanDuelContestResults', 'args': [xAuthToken] },
    { 'baseFilename': 'scrapeRotoGuruDay', },
    { 'baseFilename': 'scrapeStatsNba', 'args': ['Daily', 'Player', 'Traditional', '2016']},
    { 'baseFilename': 'scrapeStatsNba', 'args': ['Season', 'Player', 'Traditional', '2016']},
    { 'baseFilename': 'scrapeStatsNba', 'args': ['Season', 'Player', 'Advanced', '2016']},
    { 'baseFilename': 'scrapeStatsNba', 'args': ['Season', 'Player', 'Defense', '2016']},
    { 'baseFilename': 'scrapeStatsNba', 'args': ['Season', 'Player', 'PlayerBios', '2016']},
    { 'baseFilename': 'scrapeStatsNba', 'args': ['Season', 'Team', 'Traditional', '2016']},
]


for fileToRun in filesToRun:
    baseFilename = fileToRun['baseFilename']
    args = util.getObjValue(fileToRun, 'args', [])

    fullPathFilename = util.createFullPathFilename(PYTHON_SOURCE_DIR, util.createPyFilename(baseFilename))
    util.headsUp('Executing file: ' + fullPathFilename + '...')

    sys.argv = [fullPathFilename]
    sys.argv.extend(args)
    execfile(fullPathFilename)

    util.sleep(10)
    print '\n'
