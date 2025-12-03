'''
    Implemente uma classe chamada Produto com: 

    Atributos: nome, preco e estoque. 

    Um método chamado vender que reduz o estoque ao vender o produto, se houver unidades disponíveis. 

    Um método chamado repor que aumenta o estoque ao receber novas unidades. 
'''
class Produto:
    def __init__(self, nome, preco: float, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
    def vender(self, quantidade):
        if quantidade < self.estoque:
            self.estoque -= quantidade
            print('venda possivel')
        else:
            print('venda inconcluida')
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