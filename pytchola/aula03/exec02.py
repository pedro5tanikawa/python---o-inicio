'''
2. Escreva um programa que exiba a tabuada de multiplicação de um número digitado pelo usuário, de 1 a 10.
'''
multiplica = int(input('Qual numero voce deseja ver a tabuada de 1 a 10?'))
i = 1
while i < 11:
    multiplicador =  i * multiplica
    print(f"{i} x {multiplica} = {multiplicador}")
    i+= 1