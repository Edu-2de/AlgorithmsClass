import sys 
from PyQt5.QtWidgets import *

from TelaVeiculo import TelaVeiculo
from TelaCarro import TelaCarro

app = QApplication(sys.argv)

#TelaVeiculo
telaVeiculo = TelaVeiculo("Cadastro de Veículo")
telaVeiculo.show()

#TelaCarro
telaCarro = TelaCarro("Cadastro de Carro: ")
telaCarro.show()

sys.exit(app.exec_())
