import funcoes
while True: 

    op = int(input('Operacao: 1 - adiconar; Operação: 2 - remover; Operação: 3 - listar')) 

    if op == 1: 

        nome = input("nome do aluno: ") 

        funcoes.adicionar(nome) 

    elif op == 2: 

        nome = input("nome do aluno: ") 

        funcoes.remover(nome) 

    elif op == 3: 

        funcoes.exibir() 

    else: 

        break 
 