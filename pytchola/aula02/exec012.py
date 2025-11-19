'''
12) ler 3 valores e verificar se podem ser lados de um triangulo e informar caso afirmativo, qual é o triangulo 
'''
ladoA = float(input('Vamos calcular se seu triangulo funciona e, se sim, definir seu tipo. qual o tamanho do lado A? '))
ladoB = float(input('lado B? '))
ladoC = float(input('por fim, lado  C? '))
if ladoA + ladoB > ladoC and ladoA + ladoC > ladoB and ladoB + ladoC > ladoA:
    print('forma um triangulo sim! e é um:')
    if ladoA == ladoB == ladoC:
        print('triangulo equilatero! tudo inguallll')
    elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
        print('triangulo isosceles! dois lados igual')
    else:
        print('triangulo escaleno! todo mundo diferente!')
else:
    print('sai dai po, isso n existe nao')