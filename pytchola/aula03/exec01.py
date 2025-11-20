'''
Escreva um programa que receba números inteiros do usuário até que um número negativo seja digitado. Exiba a soma de todos os números positivos digitados. 
'''
contador = int(input('digite um numero: '))
soma = 0
while contador >= 0:
    soma += contador
    contador = int(input('another one: '))
print(f'a soma total de seus valores enquanto ce nao digitou um negativo: {soma} ')
    
