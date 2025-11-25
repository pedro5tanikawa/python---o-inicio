'''
    Dado este dicionário: 

pessoa = {"nome": "Ana", "idade": 25, "cidade": "Rio de Janeiro"} 
Altere a idade para 26 e a cidade para "São Paulo". Depois imprima o dicionário modificado. 
'''

pessoa = {"nome": "Ana", "idade": 25, "cidade": "Rio de Janeiro"} 
pessoa["idade"] = 26
pessoa.update({"cidade" : "rj"})
print(pessoa)