'''
21. Conte quantas vogais há em uma palavra 
'''
palavra = input('digite uma palavra: ')
vogais = ['a','e','i','o','u']
contador = 0
for letras in palavra:
    if letras in vogais:
        contador += 1
print(f'a palavra tem um total de: {contador} vogais')