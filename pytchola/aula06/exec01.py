'''
    Crie uma classe chamada Pessoa com os atributos nome e idade. Adicione um método chamado exibir_informacoes que exibe o nome e a idade da pessoa. 
'''
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def exibir_info(self):
        print(f'Nome: {self.nome} | Idade: {self.idade}')
name = input('informe seu nome: ')
age = input('informe sua idade: ')
pessoa1 = Pessoa(name,age)
#print(f'Nome: {pessoa.nome} | Idade: {pessoa.idade}')
pessoa1.exibir_info() #o () indica pro programa que é uma funçao