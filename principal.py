#!/usr/bin/env python
#By Arthur Aires
# i <3 Python
#Este script tem como objetivo,acessar a internet e por meio de buscadores
#baixar a musica que voce digitou....

import core_krafta
import download
from sys import exit
import urllib2
import multiprocessing.pool
import multiprocessing


print '[+]Bem Vindo ao Script Simple-Music-Downloader v0.1!\n'
print '[+]By Rei_Gelado - Arthur Aires\n'

ice = core_krafta.server_krafta()
gelo = download.download()

nome = raw_input('[+]Nome da Musica : \nR:')

pool = multiprocessing.pool.ThreadPool(processes=1)

url1 = None

processo  = pool.apply_async(ice.krafta,(nome,url1,1,))
 
html = processo.get()

processo = pool.apply_async(ice.krafta_compile,(html,1))

find_nome = processo.get()

processo = pool.apply_async(ice.krafta_compile_url,(html,1,))

find_url = processo.get()

print '[+]Foram parseados os seguintes resultados!\n'

for index in range(0,20):
	try:
		print '[+]Nome :' + find_nome[index] + ' - ' + find_url[index] + '\n'
	except:
		print '[+]Sem Index!\n'

print '[+]Obs se existirem valores "Sem Index" o script achou menos de 20 musicas!\n'
download_y_o_n = raw_input('\n[+]Voce deseja baixar todas as Musicas?(S\\N)\n[+]Se voce optar por nao , o script vai baixar somente a primeira!\n\nR: ')

if download_y_o_n == 'S':
	download_20 = True
elif download_y_o_n == 'N':
	download_20 = False
else:
	print '[+]Opcao Invalida!'
	#exit()


if download_20 == False:
	
	processo = pool.apply_async(ice.krafta,('None',find_url[0],2,))

	html_novo = processo.get()

	processo =  pool.apply_async(ice.krafta_compile_url,(html_novo,2,))

	link_download = processo.get()

	processo = pool.apply_async(ice.krafta,('None',link_download[0],2,))

	link_download_html = processo.get()

	processo = pool.apply_async(ice.krafta_compile_url,(link_download_html,3))

	link_download = processo.get()

	nome_do_arquivo = raw_input('[+]Qual o nome do arquivo que voce deseja salvar?\nR:')

	nome_do_arquivo = nome_do_arquivo + '.mp3'
 	
	processo = multiprocessing.Process(target = gelo.krafta_download,args = (nome_do_arquivo,link_download[0]))

	processo.start()

elif download_20 == True:

	print '[+]Essa funcao,exige um computador que tenha um hardware melhor e boa conexao com internet...!\n'
	print '[+]FUNCAO EM FASE BETA!\n'

	deseja = raw_input('[+]Deseja continuar?(S\\N) \nR:')

	if deseja == 'S' or 's':
		print '[+]Iniciando for...'
		pass
	elif deseja == 'N' or 'n':
		print '[+]Ok =)'
		exit()
	else:
		print '[+]Como voce veio para aqui?'
		exit()
	for index_download in range(0,10):
		print '[+]Iniciando Downloads.....!\n'

		print '[+]Pegando Links......!\n'
		processo = pool.apply_async(ice.krafta,('None',find_url[index_download],2,))

		html_novo = processo.get()

		processo =  pool.apply_async(ice.krafta_compile_url,(html_novo,2,))

		link_download = processo.get()

		processo = pool.apply_async(ice.krafta,('None',link_download[0],2,))

		link_download_html = processo.get()

		processo = pool.apply_async(ice.krafta_compile_url,(link_download_html,3))

		link_download = processo.get()

		if index_download == 0:
			nome_do_arquivo = raw_input('[+]Qual o nome do arquivo que voce deseja salvar?\nR:')
		else:
			pass

		nome_do_arquivo = nome_do_arquivo + '_' + str(index_download) + '_' + '.mp3'

		print '[+]Iniciando Thread para Download .......!\n'

		processo = multiprocessing.Process(target = gelo.krafta_download,args = (nome_do_arquivo,link_download[0]))

		processo.start()
