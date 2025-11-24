'''
11. Crie um programa que calcule o consumo total de energia de vários aparelhos em uma casa. Pergunte o consumo de cada aparelho em kWh e a quantidade de horas que o aparelho fica ligado por dia. O programa deve somar o consumo diário de todos os aparelhos e calcular o custo total de energia no mês. 
'''

totalDiario = 0
precokwh = 0.60
while True:
    entrada = float(input('digite o consumo em kwh(0 para encerrar): '))
    if entrada == 0:
        break
    horas = float(input("Quantas horas por dia ele fica ligado? "))
    consumo_diario = entrada * horas
    totalDiario += consumo_diario
    print(f'consumo diario desse aparelho: {consumo_diario:.2f} kwh')
consumo_mensal = totalDiario * 30
custo = consumo_mensal * precokwh

print("=== RESULTADOS ===")
print(f"Consumo diário total: {totalDiario:.2f} kWh")
print(f"Consumo mensal total: {consumo_mensal:.2f} kWh")
print(f"Custo mensal estimado: R$ {custo:.2f}")
