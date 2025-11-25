'''
    No dicionário pessoa, remova a chave "idade" usando del. Imprima o dicionário resultante. 
'''
pessoa = {"Nome": "Ana", "Idade": 25, "Cidade": "Rio de Janeiro"} 
pessoa["Idade"] = 26
pessoa.update({"Cidade" : "RJ"})
pessoa['Profissão'] = "Professora"
del pessoa["Idade"]
print(pessoa)