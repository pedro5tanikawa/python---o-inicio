'''
7. Leia o nome do time de 10 torcedores, e ao final informe quantos são flamenguistas, vascaínos, tricolores, botafoguenses, ou outro time. 
'''
fla = 0
vas = 0
flu = 0
bota = 0
outros = 0
contador = 0
while contador < 10:
    torcida  = input('qual teu time?')
    contador += 1
    if torcida == "flamengo":
        fla += 1
    elif torcida == 'vasco':
        vas += 1
    elif torcida == 'fluminense':
        flu += 1
    elif torcida == 'botafogo':
        bota += 1
    else:
        outros += 1
print(f'flamenguistas: {fla}, vascainos: {vas}, tricolores: {flu}, botafoguenses: {bota}, outros: {outros}')
