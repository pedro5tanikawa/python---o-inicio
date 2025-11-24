'''
20. Solicite números até o usuário digitar 999 e informe o menor digitado 
'''
numeros = []
while True:
    num = int(input('digite um numero(999 caso queria parar): '))
    if num == 999:
        break
    numeros.append(num)
menor = min(numeros)
print(f'dentre os numeros digitados, o menor foi o: {menor}')