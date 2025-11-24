'''
29. Leia números até digitar 0 e exiba quantos são pares e quantos são ímpares 
'''
numpar = 0
numimpar = 0
while True:
    num = int(input('digite numeros e eu retornarei quantos sao pares e quantos sao impares(digite "000" para encerrar)'))
    if num == 000:
        break
    if num % 2 == 0:
        numpar += 1
    elif num % 2 != 0:
        numimpar += 1
print(f"a quantia de numeros pares foi: {numpar}/ a quantia de numeros impares foi: {numimpar}")
    
