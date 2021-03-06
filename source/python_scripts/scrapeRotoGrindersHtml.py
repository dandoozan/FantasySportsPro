from bs4 import BeautifulSoup
import scraper
import _util as util

PARENT_DIR = 'data/rawDataFromRotoGrinders'
FILENAME = util.formatDate(util.getTodayAsDate())
SLEEP = 5

pagesToScrape = [
    {
        'dirName': 'BackToBack',
        'tableClassName': 'tbl',
        'url': 'https://rotogrinders.com/pages/nba-back-to-back-tool-518716',
    },
    {
        'dirName': 'OptimalLineup',
        'tableClassName': 'tbl',
        'url': 'https://rotogrinders.com/projected-stats/nba/lineup?site=fanduel',
    },
    {
        'dirName': 'SalaryChartsC',
        'tableClassName': 'data-table',
        'url': 'https://rotogrinders.com/pages/nba-player-salary-charts-centers-1010477',
    },
    {
        'dirName': 'SalaryChartsPF',
        'tableClassName': 'data-table',
        'url': 'https://rotogrinders.com/pages/nba-player-salary-charts-power-forwards-1010479',
    },
    {
        'dirName': 'SalaryChartsPG',
        'tableClassName': 'data-table',
        'url': 'https://rotogrinders.com/pages/nba-player-salary-charts-point-guards-1010472',
    },
    {
        'dirName': 'SalaryChartsSF',
        'tableClassName': 'data-table',
        'url': 'https://rotogrinders.com/pages/nba-player-salary-charts-small-forwards-1010480',
    },
    {
        'dirName': 'SalaryChartsSG',
        'tableClassName': 'data-table',
        'url': 'https://rotogrinders.com/pages/nba-player-salary-charts-shooting-guards-1010481',
    },
]

def getColNames(table):
    colNames = []

    #first look for ths
    ths = table.thead.tr.find_all('th')
    if len(ths) == 0:
        #if no ths, then look for tds
        ths = table.thead.tr.find_all('td')

    for th in ths:
        colNames.append(scraper.getText(th))
    return colNames

def getRowData(table):
    rowData = []
    trs = table.tbody.find_all('tr')
    for tr in trs:
        thisRowData = []
        tds = tr.find_all('td')
        for td in tds:
            thisRowData.append(scraper.getText(td))
        rowData.append(thisRowData)
    return rowData

def parseData(data, tableClassName):
    #print '    Parsing data...'
    colNames = None
    rowData = None
    soup = BeautifulSoup(data, 'html.parser')
    table = soup.find('table', class_=tableClassName)
    if table:
        colNames = getColNames(table)
        rowData = getRowData(table)
    else:
        util.headsUp('No table found')
    return colNames, rowData

def createFilename(parentDir, dirName, baseFilename):
    return parentDir + '/' + dirName + '/' + baseFilename + '.csv'

def writeData(colNames, rowData, fullPathFilename):
    #print '    Writing data to ' + fullPathFilename + '...'

    f = open(fullPathFilename, 'w')

    #write colnames
    f.write(','.join(colNames) + '\n')

    #write rows
    for row in rowData:
        f.write(','.join(row) + '\n')

    f.close()

#=============== Main ================

for page in pagesToScrape:
    dirName = page['dirName']
    tableClassName = page['tableClassName']
    url = page['url']

    print 'Scraping %s...' % dirName

    pageSource = scraper.downloadPageSource(url)
    colNames, rowData = parseData(pageSource, tableClassName)
    if colNames and rowData:
        writeData(colNames, rowData, createFilename(PARENT_DIR, dirName, FILENAME))
    else:
        util.headsUp('No data was parsed, not writing data')

    util.sleep(SLEEP)

print 'Done!'
