'''
9. Escreva um programa para ler o salário e o sexo de vários funcionários (defina uma cláusula para terminar a leitura) ao término, informar a média de salário de homens e mulheres 
'''
funcionarios = 0
masc = 0
fem = 0
salM = 0
salF = 0
while True:
    genero = input('boa noite. qual seu genero hm? ')
    if genero == "fim":
        break
    salario = float(input('e qual seu salario, bençao de deus? R$'))
    if genero == "masc":
        masc += 1
        salM += salario
    elif genero == "fem":
        fem += 1
        salF += salario
    funcionarios += 1
if masc > 0: mediaM = salM / masc
else: mediaM = 0
if fem > 0: mediaF = salF / fem
else: mediaF = 0
print(f'a quantidade de funcionarios é: {masc}, e a media salarial deles é: R${mediaM:.2f}')
print(f'a quantidade de funcionarias é: {fem}, e a media salarial delas é de: R${mediaF:.2f}')