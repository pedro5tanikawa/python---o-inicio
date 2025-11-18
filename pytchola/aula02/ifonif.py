idade = int(input('informe a idade:'))
if idade >= 18:
    print('naior de idade')
    if idade > 65:
        print('vale idoso disponivel')
    else:
        print('inda paga idade')
else:
    print('menor de idade')