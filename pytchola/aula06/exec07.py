'''
 Crie uma classe Tarefa com os atributos descricao e status (inicialmente "pendente"). Adicione métodos para:

a. Alterar o status para "concluída" (marcar_como_concluida).

b. Exibir os detalhes da tarefa (exibir_tarefa).
'''
class Tarefa:
    def __init__(peps, descricao):
        peps.descricao = descricao
        peps.status = "pendente"
    def conclusor(peps):
        peps.status = "concluida"
    def exibidor(peps):
        print(f'tarefa{peps.descricao}, status: {peps.status}')

descricao = Tarefa('estudar python')
tarefa = Tarefa(descricao)
tarefa.exibidor()
tarefa.conclusor()
