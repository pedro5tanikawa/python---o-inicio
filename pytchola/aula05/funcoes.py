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

funcionarios = []
with open("funcionarios.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        nome, idade = linha.split(',')
        idade = int(idade)
        funcionarios.append([nome,idade])

print('\nFuncionarios cadastrados:')
for f in funcionarios:
    print(f'{f[0]} - {f[1]} anos')

soma = 0
for f in funcionarios:
    soma += f[1]
media = soma / len(funcionarios)
print(f'a media das idades dos funcionarios é: {media:.2f} anos\n')

while True:
    print("\nMenu:")
    print("1 - Adicionar funcionário")
    print("2 - Remover funcionário")
    print("3 - Salvar e sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        funcionarios.append([nome, idade])
        print("Funcionário adicionado!")

    elif opcao == "2":
        print("\nFuncionários:")
        for i, f in enumerate(funcionarios):
            print(f"{i} - {f[0]} ({f[1]} anos)")

        indice = int(input("Digite o número do funcionário para remover: "))
        if 0 <= indice < len(funcionarios):
            removido = funcionarios.pop(indice)
            print(f"{removido[0]} removido!")
        else:
            print("Índice inválido.")

    elif opcao == "3":
        # Salvar no arquivo novamente
        with open("funcionarios.txt", "w", encoding="utf-8") as arquivo:
            for f in funcionarios:
                arquivo.write(f"{f[0]},{f[1]}\n")

        print("Alterações salvas. Saindo...")
        break

    else:
        print("Opção inválida.")

