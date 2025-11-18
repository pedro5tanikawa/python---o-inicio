'''
3) Crie um programa que leia um valor em reais (R$) e mostre o valor convertido em dólares
'''
real = float(input('qual o valor em Reais que sera convertido em dolar?'))
dolar = float(input('e qual valor atual do dolar?'))
conversor = real / dolar
print(f"Seu valor convertido para Dolares ficará em: US$ {conversor:.2f}".replace('.', ','))
