'''
Um determinado prêmio de loteria saiu para um bolão de três amigos. Uma lei
garante que todo prêmio de loteria deva pagar um imposto de 7% para os
cofres estaduais. Do total descontado o imposto, os amigos irão dividir o
prêmio da seguinte maneira:
● O primeiro ganhador receberá 46%;
● O segundo receberá 32%;
● O terceiro receberá o restante; Faça um programa que leia o valor total
do prêmio, calcule o desconto, o valor que cada um tem direito e
imprima o total do prêmio, o prêmio descontado o imposto e a quantia
recebida por cada um dos ganhadores.
'''
premiocru = float(input('qual o valor total do premio adquirido:'))
leao = 0.07
valorImposto = premiocru * leao
premioLiquido = premiocru - valorImposto
ganhador1 = premioLiquido * 0.46
ganhador2 = premioLiquido * 0.32
ganhador3 = premioLiquido * 0.22
print("Valor total do premio:",premiocru)
print('valor do imposto de 7%: ',valorImposto)
print('Valor do premio apos os impostos deduzidos: ', premioLiquido)
print("Ganhador 1 recebe:", ganhador1)
print("Ganhador 2 recebe:", ganhador2)
print("Ganhador 3 recebe:", ganhador3)
