'''
4) Crie um programa que leia três notas de um aluno e calcule a média aritmética.
'''
nota1 = int(input('qual a a primeira nota a ser somada?'))
nota2 = int(input('qual a segunda nota a ser somada?'))
nota3 = int(input('por fim, qual a terceira nota?'))
media = (nota1 + nota2 + nota3) / 3
print(f'a media do aluno sera:{media:.1f}')