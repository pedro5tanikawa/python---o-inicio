class Funcionario:
    def __init__(self, nome, valor_hr):
        self.nome = nome
        self.horas_trabalhadas = 0
        self.valor_hr = valor_hr
    def registrador(self,horas):
        self.horas_trabalhadas += hora
        print(f'{horas} hora(s) registradas para {self.nome}')

    def cal_pagamento(self):
        return self.horas_trabalhadas * self.valor_hr

funcionario = Funcionario('maria', 20)
funcionario.registrador(8)
funcionario.registrador(5)
print(f'Pagamento: R$ {funcionario.cal_pagamento():.2f}')
