'''
    Crie uma classe chamada Pessoa com os atributos nome e idade. Adicione um método chamado exibir_informacoes que exibe o nome e a idade da pessoa. 
'''
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def exibir_info(self):
        print(f'Nome: {self.nome} | Idade: {self.idade}')
pessoa = Pessoa('Pedrinho',26)
#print(f'Nome: {pessoa.nome} | Idade: {pessoa.idade}')
pessoa.exibir_info() #o () indica pro programa que é uma funçao