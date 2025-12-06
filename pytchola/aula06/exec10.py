class Filme:
    def __init__(self, titulo, genero, duracao):
        self.titulo = titulo
        self.genero = genero
        self.duracao = duracao
    def __str__(self):
        return f'Film {self.titulo}, genero: {self.genero}, Duração: {self.duracao} minutos'


filme = Filme('inception', 'ficcao cientifica', 148)
print(filme)