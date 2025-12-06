'''
Crie uma classe ItemEstoque com os seguintes atributos: nome, quantidade e preco_unitario. Adicione os métodos:

a. adicionar_estoque(quantidade) para aumentar o estoque.

b. remover_estoque(quantidade) para reduzir o estoque, verificando a quantidade disponível.

c. calcular_valor_total() que retorna o valor total do estoque.
'''
class ItemEstoque:
    def __init__(self, nome, quantidade, preco_unitario):
        self.nome = nome
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario
    def adicionador(self,quantidade):
        self.quantidade += quantidade
        print(f'{quantidade} unidades de {self.nome} adicionadas ao estoque!')

    def removedor(self, quantidade):
        if(quantidade <= self.quantidade):
            self.quantidade += quantidade
            print(f"{quantidade} unidades de {self.nome} removidas do estoque")
        else:
            print("transação impossivel, nao é possivel reduzir mais o estoque.")

    def calculador(self):
        return self.quantidade * self.preco_unitario
item = ItemEstoque('caneta',50, 1.50)
item.adicionador(20)
item.removedor(30)
print(f'Valor total do estoque: R${item.calculador():.2f}')