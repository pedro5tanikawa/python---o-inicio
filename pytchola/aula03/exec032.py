'''
32. Leia 10 preços e diga qual o maior e o menor 
'''
precos = []
contador = 0
while contador < 11:
    valores = float(input('digite ate 10 valores e eu vou ver aqui qual o maior e qual o menor: '))
    precos.append(valores)
    contador += 1
maior = max(precos)
menor = min(precos)
print(f'dentre os preços que voce digitou, o maior foi: {maior:.2f}')
print(f'e o menor valor foi: {menor:.2f}')