'''
5) Escreva um programa que leia o valor de um produto e o percentual de desconto. O programa deve exibir o valor final com o desconto aplicado. 
'''
ValProd = float(input('Digite o valor do produto a ser calculado: R$'))
ValDesc = float(input('Digite agora o valor do desconto de forma decimal: R$'))
descontador = ValDesc / 100
prodDesc = ValProd * descontador
valFinal = ValProd - prodDesc
print(f'Seu produto com o desconto aplicado')