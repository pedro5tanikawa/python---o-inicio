'''
24. Leia vários nomes até digitar “sair”, e conte quantos foram digitados 
'''
nomes = []
while True:
    inserir = input('digite nomes: ')
    if inserir == "sair":
        break
    nomes.append(nomes)

print(f"Foram inseridos {len(nomes)} nomes.")
