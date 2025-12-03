#Classe é o que vai estruturar o objeto
#Objeto é a instancia da classe
#Atributos são as caracteristicas do objeto
#Métodos são as ações que o objeto pode realizar

#criando uma classe
class Pessoa: #o nome da class sempre precisa começar com letra maiuscula
    def __init__(self, nome, idade): #init vai ser o constructor, como voce preenchera esses dados
        self.nome = nome 
        self.idade = idade

class Carro:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano
    def exibir_info(self):
        print(f'Carro: {self.modelo}, Ano: {self.ano}')
    def acelerar(self):
        print(f'O carro: {self.modelo} está acerelando vrummmmmmm') 
             
pessoa1 = Pessoa('ana', 25)
print(pessoa1.nome, pessoa1.idade)

carro1 = Carro('Fiat Uno', 1986)
carro1.exibir_info()
carro1.acelerar()