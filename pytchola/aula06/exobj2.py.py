# modelo com herança
class Animal:
    def __init__(self, nome):
        self.nome = nome

class Cachorro(Animal):
    def som(self):
        return 'auuuuuuuu'

class Gato(Animal):
    def som(self):
        return 'miaaaaaaaaaaaaau'
dog = Cachorro('Rex')
print(dog.nome, dog.som())
cat = Gato('felix')
print(cat.nome, cat.som())