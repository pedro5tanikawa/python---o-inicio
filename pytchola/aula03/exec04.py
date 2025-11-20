'''
4. Solicite ao usuário 5 números e exiba a soma total, usando um loop 
'''
soma = 0
contador = 0
while contador < 5:
    somaguy  = float(input("Digite um número:"))
    soma += somaguy
    contador += 1

print(f"A soma dos 5 valores é: {soma}")