import re
from bs4 import BeautifulSoup
import json
import scraper
import _util as util
import _fanDuelCommon as fd

#This file does the following:
#1. scrape 'Daily Fantasy Tournament Links - [Date]' url from https://rotogrinders.com/threads/category/main
#2. scrape contest urls from 'Daily Fantasy Tournament Links - [Date]' page
#3. for each contest
    #-download its results from api.fanduel.com

TEST = False

RG_FORUM_URL = 'https://rotogrinders.com/threads/category/main'
TODAY = util.getTodayAsDate()
YESTERDAY = TODAY - util.getOneDay()
PARENT_DIR = 'data/rawDataFromFanDuel/ContestResults/' + util.formatDate(YESTERDAY)
SLEEP = 10

def isContestLinksUrl(url, date):
    #https://rotogrinders.com/threads/daily-fantasy-tournament-links-saturday-october-29th-1512252
    dateStr = util.formatDate(date, '%A-%B-%-d').lower()
    regexPattern = 'https://rotogrinders.com/threads/daily-fantasy-tournament-links-%s(st|nd|rd|th)-\d+' % dateStr
    return not not re.match(regexPattern, url)

def scrapeRotoGrinderForum(url, date):
    print 'Scraping RotoGrinder Forum...'

    pageSource = scraper.downloadPageSource(url)

    soup = BeautifulSoup(pageSource, 'html.parser')
    table = soup.find('table', class_='forum')
    if table:
        tds = table.find_all('td', class_='topic')
        for td in tds:
            atag = td.find_all('a', recursive=False)[0]
            href = atag.get('href')
            if isContestLinksUrl(href, date):
                return href

def isFanduelUrl(url):
    #https://www.fanduel.com/games/16754/contests/16754-202913340/scoring
    regexPattern = 'https://www.fanduel.com/games/\d+/contests/\d+-\d+/scoring'
    return not not re.match(regexPattern, url)

def isNbaContest(contestName):
    return contestName.find('NBA') > -1

def parseContestFromUrl(url):
    #https://www.fanduel.com/games/16754/contests/16754-202913340/scoring
    startIndex = url.find('/contests/') + 10
    endIndex = url.find('/', startIndex)
    return url[startIndex:endIndex]

def scrapeContestsFromRotoGrinder(url):
    print 'Scraping Contest Page...'

    contests = []

    pageSource = open(PARENT_DIR + '/' + util.formatDate(YESTERDAY) + '.html') if TEST else scraper.downloadPageSource(url)
    soup = BeautifulSoup(pageSource, 'html.parser')
    div = soup.find('div', class_='content')
    if div:
        atags = div.find_all('a')
        for atag in atags:
            href = atag.get('href')
            text = atag.get_text().strip()
            if isFanduelUrl(href) and isNbaContest(text):
                contests.append(parseContestFromUrl(href))

    return contests

def createFanduelApiUrl(contest):
    return 'https://api.fanduel.com/contests/' + contest

def parseContestGroup(contest):
    return contest[:contest.find('-')]

def createHeaders(contest, xAuthToken):
    contestGroup = parseContestGroup(contest)
    referer = 'https://www.fanduel.com/games/%s/contests/%s/scoring' % (contestGroup, contest)
    return fd.getHeaders(referer, xAuthToken)

#=============== Main ================

xAuthToken = util.getCommandLineArgument()

print 'Scraping contest results for yesterday:', YESTERDAY

#make dir
util.createDirIfNecessary(PARENT_DIR)

#1. scrape 'Daily Fantasy Tournament Links - [Date]' url from https://rotogrinders.com/threads/category/main
rgTournamentLinksUrl = scrapeRotoGrinderForum(RG_FORUM_URL, YESTERDAY)
if rgTournamentLinksUrl:
    print '    Found contest page: ' + rgTournamentLinksUrl
    util.sleep(SLEEP)

    #2. scrape contest urls from 'Daily Fantasy Tournament Links - [Date]' page
    contests = scrapeContestsFromRotoGrinder(rgTournamentLinksUrl)
    if len(contests) > 0:
        print '    Found %d contests' % len(contests)
        util.sleep(SLEEP)

        #3. for each contest, download its results from api.fanduel.com
        cnt = 1
        for contest in contests:
            fullPathFilename = util.createFullPathFilename(PARENT_DIR, util.createJsonFilename(contest))
            if util.fileExists(fullPathFilename):
                print 'Skipping Contest because it already exists (%d / %d): %s...' % (cnt, len(contests), contest)
            else:
                print 'Downloading Contest (%d / %d): %s...' % (cnt, len(contests), contest)

                jsonData = scraper.downloadJson(createFanduelApiUrl(contest), createHeaders(contest, xAuthToken))
                util.writeJsonData(jsonData, fullPathFilename)

                util.sleep(SLEEP)

            cnt += 1
    else:
        util.headsUp('No contests found on RotoGrinder Contest Page')
else:
    util.headsUp('No contest link found on forum')

print 'Done!'
