'''
    Com a lista palavras = ["casa", "sol", "computador", "nuvem"], crie uma nova lista contendo somente as palavras com mais de 4 caracteres. 
'''
palavras = ["casa", "sol", "computador", "nuvem"]
mais_de_4 = []
for n in palavras:
    if len(n) > 4:
        mais_de_4.append(n)
print(f'lista padrao: {palavras}')
print(f'lista apenas das palavras com mais de 4 caracteres: {mais_de_4}')