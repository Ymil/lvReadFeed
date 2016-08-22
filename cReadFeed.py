#!/usr/bin/python
'''
Libreria: LV-readFeed
Version: 0.2
Autor: Lautaro Linquiman
Lincencia: Creative Commons
'''
import os
import sys
if not (2,7) == sys.version_info[0:2]:
	print 'Version para python 2.7'
	print 'Abortando ejecucion'
	sys.exit()

try:
	import urllib2
except ImportError:
	print 'Debes instalar el modulo urllib2'
	print 'pip install urllib2'
	sys.exit()

try:
	from bs4 import BeautifulSoup
except:
	print 'Debes instalar el modulo beautifulsoup4'
	print 'pip install beautifulsoup4'
	sys.exit()

class readFeed:
	def __downloadFeed(self):
		#Descarga el contenido del feed
		try:
			f = urllib2.urlopen(self.__url)
			self.__sourceCode = f.read()
		except:
			raise Exception('DownloadError')

	def __getContentFeed(self):
		#Traduce las variables del feed a listas
		self.__source = BeautifulSoup(self.__sourceCode)

		if(self.__type == 'rss'):
			channel = self.__source.select('channel')[0]
			self.__chanelInfo['title'] = channel.select('title')[0].get_text()
			self.__chanelInfo['description'] = channel.select('description')[0].get_text()
			self.__chanelInfo['link'] = channel.select('link')[0].get_text()
			self.__chanelInfo['update'] = channel.select('lastBuildDate')[0].get_text() #Problema
			self.__chanelInfo['pubDate'] = channel.select('pubDate')[0].get_text()
		elif(self.__type == 'atom'):
			self.__chanelInfo['title'] = self.__source.select('title')[0].get_text()
			self.__chanelInfo['description'] = self.__source.select('subtitle')[0].get_text()
			self.__chanelInfo['link'] = self.__source.select('link[rel="alternate"]')[0].attrs.get('href')
			self.__chanelInfo['update'] = self.__source.select('updated')[0].get_text()
			for entry in self.__source.select('entry'):
				entryTitle = entry.select('title')[0].get_text()
				entryLink = entry.select('link[rel="alternate"]')[0].attrs.get('href')
				entryDic = {'title': entryTitle, 'link': entryLink}
				self.__entries.append(entryDic)

	def getSource(self):
		return self.__sourceCode

	def getChannelInfo(self):
		return self.__chanelInfo

	def getEntries(self):
		return self.__entries

	def getEntry(self, idEntry):
		return self.__entries[idEntry]

	def startDownload(self):
		self.__downloadFeed()			
		self.__getContentFeed()

	def __add__(self, rF):
		for entry in rF.getEntries():
			self.__entries.append(entry)
			
	def __init__(self, url, typeFeed='rss'):
		self.__url = url
		self.__type = typeFeed
		self.__source = 0
		self.__sourceCode = ''
		self.__chanelInfo = {'title': '', 'description': '', 'link': '', 'update': '', 'pubDate': ''}
		self.__entries = []
