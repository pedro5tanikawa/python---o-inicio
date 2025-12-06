class Temperatura:
    def __init__(self,celsius):
        self.celsius = celsius
    def fahrenheitico(self):
        return self.celsius * 9/5 + 32
    def kelvinico(self):
        return self.celsius + 273.15
temperatura = Temperatura(25)
print(f'em fahrenheit: {temperatura.fahrenheitico():.2f}')
print(f'em kelvin: {temperatura.kelvinico():.2f}')