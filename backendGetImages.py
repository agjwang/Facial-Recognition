from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import urllib
import urllib2
import HTMLParser
import time
import sys
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class imageServer (BaseHTTPRequestServer):
	def _set_headers(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()
	def do_GET(self):
		self._set_headers()
		
	def do_HEAD(self):
		self.set_headers()
	def do_POST(self):
		ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
		if ctype == 'application/x-www-form-urlencoded':
			length = int(self.headers.getheader('content-length'))
			postvars = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
		else:
			return ''
		try:
			query = postvars['query']
			numImages = 1 #only doing first image for now
		except KeyError as err:
			return ''
		imageSrc = getFirstXImagesFromGoogle(query, numImages) #assuming one returned due to testing, only asking for onw
		self.wfile.write('"<img src="' + imageSrc + '">')

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
			return imageSrc  #using for test of sitey
	return imageArray

httpd = HTTPServer(('', 80, imageServer) #asssuming a port of 80 will be fine
httpd.serve_forever()
