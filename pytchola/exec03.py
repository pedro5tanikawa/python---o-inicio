'''
A padaria Sópão vende diariamente uma certa quantidade de pães franceses
e uma quantidade de broas. Cada pãozinho custa R$ 0,80 e a broa custa R$
2,50. Do total arrecadado, 43% corresponde aos custos de fabricação. Do
restante, Seu joão guarda 15% numa conta de poupança e 15% ele converte
em Euros para sua viagem anual. Sabe-se que 1 Euro custa R$ 4,60. Com
base nestes fatos, faça um programa para ler as quantidades de pães e de
broas, calcular a venda total de pães e broas, o custo de fabricação, quanto
irá guardar na poupança e quantos euros irá comprar. Ao final, exibir os
dados calculados
'''
diaAdiaPao = float(input('Quantos pães foram vendidos hoje?'))
diaAdiaBroa = float(input('E qual a quantidade de broas vendidas?'))
pao = 0.80
broa = 2.50
custos = 0.43
poupanca = 0.15
viagem = 0.15
vendasP = diaAdiaPao*pao
vendasB = diaAdiaBroa*broa
vendasTotal = vendasB + vendasP
custoSobVenda = vendasTotal * custos 
VendaLiquida = vendasTotal - custoSobVenda 
poupG = VendaLiquida*poupanca
poupV = VendaLiquida*viagem
valorconvertido = poupV / 4.60
print(f"Lucro total em vendas de pão: R$ {vendasP:.2f}".replace('.', ','))
print(f"Lucro total em vendas de broa: R$ {vendasB:.2f}".replace('.', ','))
print(f'Valor das vendas somadas: R${vendasTotal:.2f}'.replace('.',','))
print(f'Custos de produção: R${custoSobVenda:.2f}'.replace('.',','))
print(f'Valor líquido de lucro: R${VendaLiquida:.2f}'.replace('.',','))
print(f'Valor que será destinado a poupança de mista jhon: R${poupG:.2f}'.replace('.',','))
print(f'Valor que será destinado a viagem anual de mista jhon para o canadá: R${poupV:.2f}'.replace('.',','))
print(f'Por fim, valor destinado a viagem, já conventido para Euro: $ {valorconvertido:.2f}'.replace('.',','))