'''
13. Leia 8 números e encontre o maior deles. 
'''
cont = 0
while cont < 8: 
    maiornum = [num]
    num = int(input('digite um numero:'))
    cont += 1
   
    maior = max(maiornum)
print(maior)