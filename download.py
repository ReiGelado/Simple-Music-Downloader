import urllib2
import sys
#Tive muita luta na hora de criar esta classe de download,tive ajuda do google tambem heuehuehuehuhe
def sizeof_fmt(num, suffix='B'): #http://stackoverflow.com/questions/1094841/reusable-library-to-get-human-readable-version-of-file-size
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

class download():
	def krafta_download(self,nome,link):
		
		requisicao = urllib2.urlopen(link) #Inicia o Download
		
		arquivo = open(nome,'wb')

		meta = requisicao.info()

		tamanho_do_arquivo = int(meta.getheaders("Content-Length")[0])

		conversor = sizeof_fmt(tamanho_do_arquivo)

		print "[+] Baixando: %s  - Tamanho: %s" % (nome,conversor)

		tamanho_do_arquivo_dl = 0

		bloco = 8129

		while True:
			arquivo_sendo_baixado = requisicao.read(bloco)

			if not arquivo_sendo_baixado:
				print '[+]Download Completo!'
				break
			
			tamanho_do_arquivo_dl += len(arquivo_sendo_baixado)
			
			arquivo.write(arquivo_sendo_baixado)
			
			conversor = sizeof_fmt(tamanho_do_arquivo_dl)
			
			status = '[+]Nome:' + nome + '-' + 'Baixando:' + r"%s  [%3.2f%%]" % (conversor, tamanho_do_arquivo_dl * 100. / tamanho_do_arquivo) + chr(8)*(len(r"%s  [%3.2f%%]" % (conversor, tamanho_do_arquivo_dl * 100. / tamanho_do_arquivo))+1) #Pog
			
			print status + '\n',
		arquivo.close()
