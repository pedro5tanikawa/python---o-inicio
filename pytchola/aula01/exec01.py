'''
Faça um programa para calcular a quantidade de latas de tintas para pintar
uma parede. O programa deverá solicitar ao usuário, a altura (float) e o
comprimento(float) da parede. Considere que a cobertura da tinta é de 1 litro
para cada 3 metros quadrados e que a tinta é vendida em latas de 3,6 litros,
que custam R$ 107,00. Informe ao usuário a quantidades de latas de tinta a
serem compradas e o preço total.
'''


alt = float(input('qual a altura da parede a ser pintada?'))
comp = float(input('agora, o comprimento da parede'))
area = alt * comp 
print(area)
litros = area / 3 #litros gastos
resultado1 = round(litros)
print(resultado1)
tinta = 3.6
lata = round(litros) / tinta
resultado2 = round(lata)
print(resultado2) #aqui vai imprimir a quantidade de latas
tintaVAL = round(lata) * 107
print('numero latas:',resultado2)
print('valor gasto:', tintaVAL)
'''
asjakshkajskahsjjc
ekckehckjehdcjhekchkecd
ecbkecjehckhdjk
edjl
'''
