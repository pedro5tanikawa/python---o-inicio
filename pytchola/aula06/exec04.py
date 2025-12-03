'''
Crie uma classe Estudante com atributos nome e notas (uma lista de notas). Adicione métodos para: 
Calcular a média das notas. 
Exibir uma mensagem dizendo se o estudante foi aprovado (média >= 6) ou reprovado. 
'''
class Estudante:
    def __init__(self,nome,notas):
        self.nome = nome
        self.notas = notas
    def media(self):
        return sum(self.notas) / len(self.notas)
    def __str__(self):
        return f'Aluno: {self.nome} | '