import sys 
from PyQt5.QtWidgets import *
from Categoria import Categoria
from TelaCarro import TelaCarro

class TelaCategoria (QMainWindow):

    def __init__(self, titulo = "Tela Veículo", categorias = [], telaCarro = None):
        self.listaCategorias = categorias
        self.telaCategoria = telaCarro

        super().__init__()

        self.setWindowTitle(titulo)
        self.setGeometry(100, 150, 200, 100) #setGeometry(x, y, largura, altura)
        self.layout = QVBoxLayout()

        self.definirLayout()
        #botão
        self.btnSalvar = QPushButton("Salvar", self) #o botão de salvar recebrá a classe de pyqt5 QPushButton com o "salvar, que é minha função definida no código abaixo"
        self.btnSalvar.clicked.connect(self.__salvar)#programei para quando este botão for clicado ele irá conectar à função salvar dentro do próprio método construtor.
        self.layout.addWidget(self.btnSalvar)#estou afirmando que o layout receberá um widget, que é o botão que criei acima.

        container = QWidget() #Criei um container com a classe QWdiget
        container.setLayout(self.layout) #setei o layout
        self.setCentralWidget(container) #Defini que este widget é central
    
    def definirLayout(self):
        self.lblNome= QLabel("Nome: ")
        self.txtNome = QLineEdit(self)

        self.layout.addWidget(self.lblNome) 
        self.layout.addWidget(self.txtNome)
    
    #implementar o botão salvar
    def __salvar(self):
        nome = self.txtNome.text() 
        
        if(nome != ""): 
            cat = Categoria( nome )
            self.listaCategorias.append(cat)
            # self.telaCarro.carregarCategorias()
        QMessageBox.information(self, "Categoria salva", str(cat) )