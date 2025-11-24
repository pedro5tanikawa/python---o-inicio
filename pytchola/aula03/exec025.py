'''
25. Pergunte 10 números e conte quantos são múltiplos de 3 
'''
contador = 0
div_3 = 0
while contador < 10:
    numeros = int(input('digite 10 numeros e retornarei os que sao divisiveis por 3: '))
    if numeros % 3 == 0:
        div_3 += 1
    contador += 1
print(f"numeros divisiveis por 3: {div_3}")