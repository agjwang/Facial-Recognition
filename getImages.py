from bs4 import BeautifulSoup
import requests
import urllib
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
		result = requests.get('https://www.google.ca/search?q=' + query.replace(' ', '+') + '&tbm=isch')
		result.raise_for_status()
		return result.content
      	except requests.exceptions.HTTPError as err:
		print err.response.status_code
		return None

def getFirst3ImagesFromGoogle(query):
	result = searchImages(query)
	if result == None:
		print 'Search failed.'
		return
	soup = BeautifulSoup(result)
	with open('result.txt','w') as f:
		f.write(str(soup))
	imageDiv = soup.find('div', {'id':'ires'}) #expecting this id to be present in all google results
	images = imageDiv.find_all('img')
	for i in range(0, 3):
		imageSrc = images[i]['src']
		imageName = str(i) + '.jpg'
		try:
			download(imageSrc, imageName)
		except Exception as e:
			print Exception
		time.sleep(10)

getFirst3ImagesFromGoogle('Naruto')

