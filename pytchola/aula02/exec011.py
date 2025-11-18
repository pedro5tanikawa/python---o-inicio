'''
11) Crie um programa que calcule o tempo restante até a aposentadoria de uma pessoa. Pergunte a idade e o tempo de contribuição (em anos). A pessoa pode se aposentar com 35 anos de contribuição ou 60 anos de idade. Mostre o tempo restante para a aposentadoria 
'''
idade = int(input('qual a sua idade?'))
tempoC = int(input('e qual o seu tempo total de contribuiçao ate hoje? diga em anos'))
if idade >= 60:
    print('voce esta pronto para se aposentar!')
else:
    