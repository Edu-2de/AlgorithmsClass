class Carro:
    def __init__(self, modelo=None, ano=2025, placa = None):
        self.modelo = modelo
        self.ano = ano
        self.placa = placa
        self.prox = None

    def __str__(self):
        return self.modelo + " - ano: " + str(self.ano) + " - " + self.placa