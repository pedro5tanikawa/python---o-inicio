def cumprimentar(nome:str, hora:int):
    if hora <12:
        return f'bom dia, {nome}'
    elif hora < 18:
        return f'boa tarde, {nome}'
    else:
        return f'boa noite, {nome}'

def calculadora(num1, num2, operacao):
    if operacao == "+":
        return num1 + num2
    elif operacao == "-":
        return num1 - num2
    elif operacao == "*":
        return num1 * num2
    elif operacao == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return 'error, divisao por 0'
    else:
        return "operação invalida!"
    
alunos = [] 

def adicionar(nome): 

    alunos.append(nome) 

    print(f"Aluno {nome} adicionado") 

 

def remover(nome): 

    if nome in alunos: 

        alunos.remove(nome) 

        print(f"{nome} removido") 

    else: 

        print("Não encontrado") 

 

def exibir(): 

    print("Lista de alunos") 

    for aluno in alunos: 

        print(aluno) 

def situacao(nota1,nota2):
    media = (nota1+nota2)/2
    if media >= 6:
        return 'aprovado'
    else:
        return "reprovado"

def descontador(valor,desc):
    return (valor - (valor*(desc/100)))