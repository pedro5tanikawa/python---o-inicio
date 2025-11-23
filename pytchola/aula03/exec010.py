'''
10.  Leia o salario e o sexo de n funcionários, e ao final informe: 
- qtd de funcionários de cada sexo 
- a soma do salário das mulheres 
- a soma do salário dos homens 
- a média salarial dessa empresa 
- o programa termina quando for digitado "fim" 
'''
funcionarios = 0
masc = 0
fem = 0
salMasc = 0
salFem = 0 
while True:
            genero = input('qual seu genero? ')
            if genero == 'fim':
                break
            if genero not in ["masc", "fem"]:
                print("Opção inválida. Digite masculino, feminino ou fim.")
                continue
            salario = float(input('e qual o seu salario amigo(a): R$'))
            
            if genero == "masc":
                    masc +=  1
                    salMasc += salario
            elif genero == "fem":
                    fem += 1
                    salFem += salario
            
            funcionarios += 1
if funcionarios > 0:
    media = (salMasc + salFem) / funcionarios
else:
       media = 0
            
print(f'quantidade de funcionarios homens: {masc} e a soma de seus salarios é: {salMasc:.2f}')
print(f'a quantidade de funcionarias é: {fem} e a soma de seus salarios é: {salFem:.2f}')
print(f'a media salaria da empresa é: {media}')

            

   