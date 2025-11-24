'''
13. Leia 8 números e encontre o maior deles. 
'''
numeros = []
contador = 0
while contador < 8:
    num = int(input('digite um numero: '))
    numeros.append(num)
    contador += 1
maior = max(numeros)
print(f'dentre os 8 numeros digitados, o maior deles foi: {maior}')