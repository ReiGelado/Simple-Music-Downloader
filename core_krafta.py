#!/usr/bin/env python
#Arquivo de core do Simples-Music-Downloader

import urllib2
import cookielib
import re

class server_krafta():
	def __init__(self):
		self.download = True #WTF?
	def krafta(self,nome_da_musica,url1,id):
		header = {
				"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.46 Safari/535.11",
				"Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
				"Accept-Language" : "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
				"Accept-Charset" : "UTF-8",
				"Accept-Encoding" : "gzip, deflate",
				"Content-type" : "application/x-www-form-urlencoded",
				"Host" : "www.krafta.net",
				"Referer" : "http://google.com/"
				}
		
		biscoito = urllib2.HTTPCookieProcessor(cookielib.MozillaCookieJar())

		abrir = urllib2.build_opener(biscoito)

		nome_da_musica_encoded = nome_da_musica.split()

		nome_da_musica_enc = '+'.join(nome_da_musica_encoded)

		if id == 1:
			requisicao = urllib2.Request('http://www.krafta.net/searchSuggest.php?txtSearch=%s&cmdSearch=Search!&dosearch=dosearch' % nome_da_musica_enc)
		elif id == 2:
			requisicao = urllib2.Request(url1)

		req = abrir.open(requisicao)

		return req.read()

	def krafta_compile(self,html,id):
		if id == 1:
			compile_1 = re.compile('" rel="nofollow">(.*?)</a></b><br><br>')
			findall = re.findall(compile_1,html)
		return findall
	def krafta_compile_url(self,html,id):
		if id == 1:
			compile_1 = re.compile('   <a href="(.*?)" rel="nofollow">')
			findall = re.findall(compile_1,html)
		elif id == 2:
			compile_1 = re.compile('<a href="(.*?)" target="_blank"><img')
			findall = re.findall(compile_1,html)
		elif id == 3:
			compile_1 = re.compile('window.location = "(.*?)"')
			findall = re.findall(compile_1,html)
		return findall
