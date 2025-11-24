'''
17. Receba notas até o usuário digitar -1 e calcule a média 
'''
qtd_notas = 0
notas = 0
while True:
    nota = int(input('quais foram suas notas para que eu calcule (digite -1 para acabar): '))
    if nota == -1:
        break
    if nota > 0:
        notas += nota
        qtd_notas += 1
if qtd_notas > 0:
    media = notas / qtd_notas
    print(f'a sua media foiiiiii.........{media:.2f}')
    