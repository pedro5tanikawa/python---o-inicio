'''
23. Exiba a soma de todos os números pares entre 1 e 100. 
'''
soma = 0
for i in range(1, 101):
    if i % 2 == 0:
        soma += i
print(f"A soma dos números pares de 1 a 100 é: {soma}")
