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
premioLeao = premiocru * leao
print('valor do premio ja com impostos deduzidos:',premioLeao)
ganhador1 = 0.46
ganhador2 = 0.32
ganhador3 = premiocru - (ganhador1 + ganhador2)
print(f)
