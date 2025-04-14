import sys 
from PyQt5.QtWidgets import *

from TelaVeiculo import TelaVeiculo

class TelaCarro (TelaVeiculo):
    def __init__(self, titulo="Tela Veículo"):
        super().__init__(titulo) #função super() afirma que o init da superclasse será a mesma da declarada de quem ela herda. Neste caso, a classe TelaCarro recebe os mesmos parâmateros e funções de TelaVeiculo

    def definirLayout(self): # estou redefinindo uma função que já existe e herdei de TelaVeiculo,o nome disto é POLIMORFISMO: o ato de alterar funções de classes herdadas, mas mantendo outras comooriginalmente são.
        super().definirLayout()
        self.lblPortas = QLabel("Quantidade de portas: ")
        self.txtPortas = QLineEdit(self) #QLineEdit recebe somente o que a própria classe recebe, por isto self
        self.layout.addWidget(self.lblPortas)
        self.layout.addWidget(self.txtPortas)
