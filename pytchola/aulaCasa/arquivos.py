# open("caminho",'r')
# r - leitura
# a - append
# w - write (apaga tudo e escreve por cima)
# x - create
# r+ - leitura + escrita
# sempre que for mudar o modo de uso do arquivo, precisa mudar o comando do open
arquivo = open('pytchola/aula05/texto2.txt','w') #aqui precisa colocar o caminho correto para chamar o arquivo
#print(arquivo.readable()) aqui é para ter certeza que é legivel
#print(arquivo.read()) aqui le todo o arquivo
#print(arquivo.readline()) aqui le apenas uma linha, porem se repetir o comando, ele vai lendo linha apos linha sem repetir
#print(arquivo.readline())
#print(arquivo.readline())
#print(arquivo.readline())
#print(arquivo.readline())
#print(arquivo.readline())
#lista = arquivo.readlines() # aqui vai transformar numa lista e torna-la manipulavel
#print(lista)
#print(lista[3]) # aqui eu posso chamar o indice que eu quiser, no caso foi o terceiro
#arquivo.write('kikerson') # adicionar \n no final do que sera adicionado faz com que pule a linha
arquivo.write("misato\n")
arquivo.write('michata\n')
arquivo.write('pituca\n')
arquivo.write('putuquinha\n')
arquivo.close()