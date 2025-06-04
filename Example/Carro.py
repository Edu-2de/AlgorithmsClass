from Veiculo import Veiculo

class Carro( Veiculo ):
    def __init__(self, modelo=None, ano=2025, qtd = 4):
        super().__init__(modelo, ano)
        self.portas = qtd

    def __str__(self):
        return super().__str__() + "\nPortas: " + str( self.portas)