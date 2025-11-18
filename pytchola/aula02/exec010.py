'''
10) Considere que o preço da tarifa de energia é R$ 0,50 por kWh. 
Pergunte ao usuário o consumo de energia em kWh e calcule o valor total a ser pago pela conta. Se o consumo for maior que 200 kWh, aplique um desconto de 10%. 
'''
consumo = int(input('informe a quantidade de energia gasta em KWH'))
if consumo > 200:
   desconto = consumo*0.10
   ValConta = (consumo - desconto)*0.50
   print(f'O valor da sua conta com o desconto de 10% ficara em: R${ValConta:.2f}')
else:
    ValConta = consumo * 0.50
    print(f'O valor final da sua conta será: R$ {ValConta:.2f}')





