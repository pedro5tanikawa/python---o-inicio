'''
22. Leia 5 números e mostre quantos são negativos. 
'''
cntd = 0
negativos = 0
while cntd < 5:
    num = int(input('digite 5 numeros: '))
    if num < 0:
        negativos += 1
    cntd += 1
print(f"a quantidade de numeros negativos foi: {negativos}")