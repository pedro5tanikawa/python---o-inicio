# Dicionário de funcionários com ID, nome e cargo 
funcionarios = { 
    1: {"id": 1, "nome": "Ana", "cargo": "Desenvolvedora"}, 
    2: {"id": 2, "nome": "Carlos", "cargo": "Analista de Sistemas"}, 
    3: {"id": 3, "nome": "Luana", "cargo": "Gerente de Projetos"}, 
    4: {"id": 4, "nome": "Fernando", "cargo": "Desenvolvedor"}, 
    5: {"id": 5, "nome": "Juliana", "cargo": "Designer"} 
} 
 
# Acessando dados - exibe o nome e o cargo de um funcionário pelo ID 
funcionario_1 = funcionarios[1]  # Acessando pelo ID 
print(f"Funcionário 1: {funcionario_1['nome']} - Cargo: {funcionario_1['cargo']}") 
id_desejado = 3 
funcionario_encontrado = next((funcionario for funcionario in funcionarios.values() 
    if funcionario["id"] == id_desejado), None) 
if funcionario_encontrado: 
    print(f"Funcionário encontrado: {funcionario_encontrado['nome']} - Cargo: {funcionario_encontrado['cargo']}") 
else: 
    print(f"Funcionário com ID {id_desejado} não encontrado.") 
funcionarios[1]["cargo"] = "Líder de Desenvolvimento" 
print(f"Funcionário 1: {funcionario_1['nome']} - Cargo: {funcionario_1['cargo']}") 
 
funcionarios[6] = {"id": 6, "nome": "Lucas", "cargo": "Product Owner"} 
next_id = max(funcionarios.keys()) + 1  # Obtém o próximo ID disponíve
funcionarios[next_id] = {"id": next_id, "nome": "Lucas", "cargo": "Product Owner"} 
del funcionarios[5]  # Removendo o funcionário de ID 5 
if 3 in funcionarios: 
    print(f"Funcionário com ID 3 encontrado: {funcionarios[3]['nome']}") 
cargo_funcionario2 = funcionarios.get(8, {}).get("cargo", "ID não encontrado") 
print(f"Cargo do funcionário : {cargo_funcionario2}") 
print("\nListando todos os funcionários:") 
for id, dados in funcionarios.items(): 
    print(f"ID: {id}, Nome: {dados['nome']}, Cargo: {dados['cargo']}") 
 
print("\nFuncionários com o cargo de 'Desenvolvedor':") 
for id, dados in funcionarios.items(): 
    if dados["cargo"] == "Desenvolvedor": 
        print(f"ID: {id}, Nome: {dados['nome']}") 
 
print("\nFuncionários com o cargo de 'Desenvolvedor':") 
for id, dados in funcionarios.items(): 
    if dados["cargo"] == "Desenvolvedor": 
        print(f"ID: {id}, Nome: {dados['nome']}") 
 
