'''
    Implemente uma classe chamada Produto com: 

    Atributos: nome, preco e estoque. 

    Um método chamado vender que reduz o estoque ao vender o produto, se houver unidades disponíveis. 

    Um método chamado repor que aumenta o estoque ao receber novas unidades. 
'''
class Produto:
    def __init__(self, nome: str, preco: float, estoque: int): #pra evitar erros SEMPRE defina o tipo de conteudo que seja inserido em cada self da classe
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
    def vender(self, quantidade):
        if (quantidade < self.estoque): #o conteudo do if dentro de parenteses faz o codigo ser mais legivel, mais profissional
            self.estoque -= quantidade
            print(f'Foram vendidas {quantidade} unidade(s)')
        else:
            print('venda inconcluida, estoque insuficiente')
    def repor(self,qtd):
        if qtd > 0:
            self.estoque += qtd
            print(f'{qtd} adicionada ao estoque!')
        else:
            print('ta maluco, como tu vai adicionar uma quatidade negativa fio?! vai roba?')


produto1 = Produto('camisa',22.00,10)
produto1.vender(3)
produto1.repor(5)
print(produto1.estoque)
