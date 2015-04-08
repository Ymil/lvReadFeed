#!usr/bin/python
'''
Libreria: LV-readFeed
Version: 0.1
Autor: Lautaro Linquiman
Lincencia: Creative Commons
'''
from cReadFeed import readFeed
def main():
	feed = readFeed('http://www.tutorialdeprogramacion.com/feeds/posts/default', 'atom')
	'''Carga todas las variables nesesarias para la funcionalidad de la libreria'''

	feed.startDownload()	
	''' Descargando y estructurando el Feed 
		raise DownloadError: error de descarga del feed'''
	feed.getSource()
	''' Retorna el codigo fuente del Feed en texto plano'''
	feed.getChannelInfo()
	''' Retorna informacion del canal dic {title, descripcion, link, update} '''
	feed.getEntries()
	''' Retorna una lista con todas las entradas obtenidas del feed
		list [0:] entrada ID
			[0:] dic {title, link} '''
	feed.getEntry(1)
	''' Retorna la informacion de la entrada indicada 
		dic {title, link} '''

	#Sobre carga de la clase feed
	print 'Cantidad de entradas antes de la sobre carga ' , len(feed.getEntries())

	feed1 = readFeed('http://www.tutorialdeprogramacion.com/feeds/posts/default', 'atom') 

	feed+feed1

	print 'Cantidad de entradas despues de la sobre carga ' , len(feed.getEntries())
main()
