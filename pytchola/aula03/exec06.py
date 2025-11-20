'''
6. Escreva um programa que receba 10 números inteiros e conte quantos deles são pares. 
'''
numPar = 0
contador = 0
while contador < 10:
    somaguy  = float(input("Digite um número:"))
    contador += 1
    if somaguy % 2 == 0:
        numPar += 1
print(f'a quantidade de numero pares dentre esses 10 foi: {numPar}')