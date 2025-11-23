contador = 0
numPosi = 0

while True:
    num = input('Digite um número (0 para parar): ')
    
    if num == 0:
        print('Programa encerrado.')
        break

    if num > 0:
        numPosi += num
        contador += 1

# cálculo e saída só depois do loop
if contador > 0:
    media = numPosi / contador
    print(f'A média dos números positivos é: {media:.2f}')
else:
    print('Nenhum número positivo foi digitado.')
