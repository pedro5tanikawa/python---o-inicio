class ReservaHotel:
    def __init__(self, nome_cliente, dias_reserva, valor_diaria):
        self.nome_cliente = nome_cliente
        self.dias_reserva = dias_reserva
        self.valor_diaria = valor_diaria

    def calculador(self):
        return self_dias * valor_diaria

    def __str__(self):
        return f'Reserva: Cliente: {self.nome_cliente}, Dias: {self.dias_reserva}, Total: R${self.calculador():.2f}'
reserva = ReservaHotel('Joao', 5, 200)
print(reserva)