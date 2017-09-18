from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import urllib
import urllib2
import HTMLParser
import time
import sys

def download(src, name):
        downloadedFile = urllib.urlretrieve(src, name, progressReporter)

def progressReporter(blockNum, blockSize, totalSize):
        percent = int(blockNum*blockSize/totalSize*100)
        sys.stdout.write('\r' + 'Download: ' + str(percent) + '%')
        sys.stdout.flush()

def searchImages(query):
	try:
		driver = webdriver.Firefox()
		result = driver.get('https://www.google.ca/search?q=' + query.replace(' ', '+') + '&tbm=isch') #need selenium to get decrypted urls for the parent links
		result = driver.find_element_by_id('ires').get_attribute('innerHTML') #expecting this id to be present in all google results, has been in 10+ so far
		return result
      	except Exception as err: #cannot find selenium's HTTPError; this is better than nothing
		print err
		return None

def getFirstXImagesFromGoogle(query, numImages):
	result = searchImages(query)
	if result == None:
		print 'Search failed.'
		return
	soup = BeautifulSoup(result)
	images = soup.find_all('img')
	imageArray = []
	for i in range(0, numImages):
		parent = images[i].parent
		src = parent['href']
		encodedUrl = src[src.find('?imgurl=') + len('?imgurl='):src.find('&imgrefurl')]
		partiallyDecodedUrl = urllib2.unquote(encodedUrl).decode('utf8')
		imageSrc = HTMLParser.HTMLParser().unescape(partiallyDecodedUrl).encode(sys.getfilesystemencoding())
		imageArray.append(imageSrc)
		if numImages == 1:
			return imageArra #using for test of sitey
	return imageArray

