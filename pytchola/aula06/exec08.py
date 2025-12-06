class Carrinho:
    def __init__(self):
        self.itens = []
    
    def adicionador(self,nome,preco):
        self.itens.append({'nome': nome, 'preco': preco})
    def exibidor(self):
        for item in self.itens:
            print(f"Produto: {item['nome']}, preco: R${item['preco']:.2f}")
    def totalizador(self):
        return sum(item['preco'] for item in self.itens)
carrinho = Carrinho()
carrinho.adicionador('camiseta',29.90)
carrinho.adicionador('calça',89.90)
carrinho.exibidor()
print(f'Total: R$ {carrinho.totalizador():.2f}')
