'''
11) Crie um programa que calcule o tempo restante até a aposentadoria de uma pessoa. Pergunte a idade e o tempo de contribuição (em anos). A pessoa pode se aposentar com 35 anos de contribuição ou 60 anos de idade. Mostre o tempo restante para a aposentadoria 
'''
idade = int(input('qual sua idade, abençoado? '))
if idade >= 60:
    print('finalmente!!!!!pode se aposentar!')
    tempoTrab = int(input('Mas pera la, quanto tempo voce trabalhou? '))
    if tempoTrab >= 20:
     print(f'ah bao, entao se voce trabalhou {tempoTrab}anos, voce pode se aposentar sim, me cafundi')
    else:
     aindaFalta = 20 - tempoTrab
     print(f'hmmmm to vendo aqui que ainda faltam {aindaFalta} anos...')
else:
   aposentador = 60 - idade
   print(f'vishhhhh, ainda faltam {aposentador} anos pra voce se aposentar...')
aposentadorNormal = int(input('Ah, ce quer saber entao se dá ou nao pra se aposentar por tempo trabalhado? entao quanto tempo voce trabalhou de carteira assinada?'))
if aposentadorNormal >= 35:
     print(f'{aposentadorNormal} anos??!! caracas, quanto tempo. pode se aposentar imediatamente!')
else:
     aindaFalta2 = 35 - aposentadorNormal
     print(f'puxa.....ainda faltam {aindaFalta2} anos pra voce descansar 4real...')
