'''
    Ainda usando o dicionário pessoa (após a modificação do exercício anterior), adicione uma nova chave "profissão" com algum valor (por exemplo, "Engenheira"). Imprima o dicionário atualizado. 
'''
pessoa = {"Nome": "Ana", "Idade": 25, "Cidade": "Rio de Janeiro"} 
pessoa["Idade"] = 26
pessoa.update({"Cidade" : "RJ"})
pessoa['Profissão'] = "Professora"
print(pessoa)