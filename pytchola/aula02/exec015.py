'''
15) Solicita três notas de um aluno, calcular a média e informar se ele está aprovado ou não, considerando a média de aprovação maior ou igual a 6. 
'''
nota1 = int(input('qual a a primeira nota a ser somada?'))
nota2 = int(input('qual a segunda nota a ser somada?'))
nota3 = int(input('por fim, qual a terceira nota?'))
media = (nota1 + nota2 + nota3) / 3
if media >= 6:
    print('Parabens, voce foi aprovado!')
else:
    print('viiiiiiishhh ta de recuperaçao chefe   );')
print(f'a media do aluno sera:{media:.1f}')