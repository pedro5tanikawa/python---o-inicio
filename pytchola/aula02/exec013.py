'''
13) ler altura e peso, e informar o imc e qual a situação do indivíduo 
'''
alt = float(input('Diga-me: qual sua altura para que eu possa calcular seu IMC:'))
peso = float(input('E agora, me diga seu peso:'))
duplicador = alt*alt
imc = peso / duplicador
if  imc < 18.5:
    print(f'mano......tu ta na merda. {imc:.2f} de imc é muito baixo')
elif imc < 25:
    print(f'tudo normar chefe, seu imc é de {imc:.2f}')
elif imc < 30:
    print(f'num ta taaao ruim nao, seu imc ta {imc:.2f}')
elif imc < 35:
    print(f'pesou o clima...negocio ta ficando serio meu amigo, {imc:.2f} de imc é muita coisa!')
elif imc < 40:
    print(f'MEUAMIGO QUE ISSO CARA! {imc:.2f} DE IMC!')
