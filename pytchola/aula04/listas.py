lista = ['maça','banana','cherry']
print(len(lista))
print(lista[1])
# imprime o segundo item da lista, pois a lista sempre começa em 0
# caso ponha numero negativo, o contador vai fazer a volta na lista, no caso se for -1, a lista vai dar uma volta ao contrario, no caso o -1 sendo cherry
# se eu puser como print(lista[0:2]) vai imprimir todos os numeros, começando do 0 e indo ate o 2
# se eu nao puser o segundo numero, a contagem nao vai parar num numero especifico, vai ate o fim. se eu fizer o contrario, ele vai começar do inicio e parar no numero que eu definir
# o segundo numero ele nao é incluso, a contagem para quando chegaria nele
# listas sao [] e dicionarios sao {} set sao {} tambem
list1 = ["abc", 34, True, 40, "male"]

thislist = ["apple", "banana", "cherry"]
thislist[1] = "maçuina"
print(thislist)

list = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
list[1:3] = ["ioguirte", "watermelon"]
list.insert(1,"caju")
list.remove("mango")
# remove vai procurar o conteudo para apagar, e caso tenha mais de um igual, ele so eliminara 1
list.pop(0)
# pop vai eliminar pelo indice, voce decide o que sera eliminado e decide o indice apropriado
print(list)
# aqui voce consegue caçar palavras que tenham a letra desejada, no caso o "a" e so vai imprimir se tiver a letra a 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist) 

nums = [1, 2, 3, 4, 5, 6, 7, 8]
impares = []
for n in nums: # aqui o "n" sera cada indice, cada conteudo da lista, que passara pelo teste para ver se é divisivel ou nao por 2, se for, a lista de pares recebe esse valor novo
    if n % 2 != 0: 
        impares.append(n)

print(nums)
print(impares)