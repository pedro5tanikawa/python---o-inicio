'''
Crie uma classe Estudante com atributos nome e notas (uma lista de notas). Adicione métodos para: 
Calcular a média das notas. 
Exibir uma mensagem dizendo se o estudante foi aprovado (média >= 6) ou reprovado. 
'''
class Estudante:
    def __init__(self,nome,notas):
        self.nome = nome
        self.notas = notas
    def cal_media(self):
        return sum(self.notas) / len(self.notas)
    def aprovador(self):
        media = self.cal_media()
        if media >= 6:
            print(f'{self.nome} aprovado com media: {media:.2f}')
        else:
            print(f'{self.nome} reprovado com uma media de {media:.2f}')

lista_notas = [] # aqui, esse bloco todo sobre lista_notas, poderia estar localizado na parte de cima, que nao interferira na logica
nome = input('informe seu nome: ')
for x in range(4):
    nota = int(input('informe sua nota: ')) #  "int" pega o numero digitado (que a principio sera lido como texto) e o transforma em inteiro.
    lista_notas.append(nota)

estudante = Estudante(nome, lista_notas) # a variavel estudante PRECISA ter estar dentro da classe para que faça parte da classe
estudante.aprovador()