i = 1
while i < 6:
    print(i)
    i+= 1
    if i == 4:
        print('passou pelo numero quatro')
'''
aqui ele apenas avisa caso ele passe pelo numero 4, pq a condição if ta verificando se o i é igual ao 4
'''

#ex:. parar o while

z = 1
while z < 6:
  print(i)
  if z == 3:
    break
  z += 1 
'''
aqui, o programa encerra quando a contagem chega a 3, mesma situação que a anterior, depende da analise do if
'''
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

'''
aqui ele vai voltar ao inicio da contagem quando o i for igual a 3
'''