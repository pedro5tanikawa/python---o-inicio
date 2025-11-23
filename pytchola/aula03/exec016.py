x = 0
maior = 0

while x < 6:
    idade = int(input('Qual sua idade? '))
    
    if idade >= 18:
        maior += 1

    x += 1

print('Quantidade de maiores de idade:', maior)
