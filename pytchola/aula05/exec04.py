with open('teste.txt','r',encoding='utf-8') as arq:
    linhas = arq.readlines()
soma = 0
quantidade = 0
for linha in linhas:
    nome,preco = linha.strip().split(',')
    soma += float(preco)
    quantidade += 1
media = soma/quantidade
print(f'preço medio: R${media}')