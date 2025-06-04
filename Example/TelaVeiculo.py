import sys 
from PyQt5.QtWidgets import *
from Veiculo import Veiculo

class TelaVeiculo(QMainWindow):

    def __init__(self, titulo = "Tela Veículo"):
        super().__init__()

        self.setWindowTitle(titulo)
        self.setGeometry(100, 150, 300, 150) #setGeometry(x, y, largura, altura)
        self.layout = QVBoxLayout()

        self.definirLayout()
        #botão
        self.btnSalvar = QPushButton("Salvar", self) #o botão de salvar recebrá a classe de pyqt5 QPushButton com o "salvar, que é minha função definida no código abaixo"
        self.btnSalvar.clicked.connect(self.salvar)#programei para quando este botão for clicado ele irá conectar à função salvar dentro do próprio método construtor.
        self.layout.addWidget(self.btnSalvar)#estou afirmando que o layout receberá um widget, que é o botão que criei acima.

        container = QWidget() #Criei um container com a classe QWdiget
        container.setLayout(self.layout) #setei o layout
        self.setCentralWidget(container) #Defini que este widget é central
    
    def definirLayout(self):
        self.lblModelo = QLabel("Modelo: ")#afirmei que a label do modelo é a classe QLabel que recebe um texto como argumento. QLabel é uma classe da biblioteca PyQT5
        self.txtModelo = QLineEdit(self)#afirmei que o texto do modelo é a classe QLineEdit que recebe um texto como argumento. QLineEdit é uma classe da biblioteca PyQT5
        self.lblAno = QLabel("Ano: ") # Mesma lógica acima
        self.txtAno = QLineEdit(self) # Mesma lógica acima

        self.layout.addWidget(self.lblModelo) #estou afirmando que o layout é um widget que adiciona a label de Modelo
        self.layout.addWidget(self.txtModelo)
        self.layout.addWidget(self.lblAno)
        self.layout.addWidget(self.txtAno)
    
    #implementar o botão salvar
    def salvar(self):
        modelo = self.txtModelo.text() #modelo recebeu o QLineEdit, que é classe contendo um texto com as dimensões, com o final .text() eu estou afirmando que esta variável recebe somente a parte de texto da classe QLineEdit.
        ano = self.txtAno.text() #mesma lógica.
        if(ano != ""): #se o ano não for vazio,
            ano = int(ano) #variável ano recebe o ano como um número inteiro,
        veiculo = Veiculo(modelo, ano) #variável veículo recebe a classe Veiculos com as variáveis definidas na função (modelo, ano) que são os parâsmetros que ela normalmente recebe.
        QMessageBox.information(self, "Veículo salvo", str(veiculo) )
