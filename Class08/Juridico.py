from Cliente import Cliente

class Juridico( Cliente ):

    def __init__(self, nome = None, cnpj = None):
        super().__init__(nome)
        self.cnpj = cnpj

    def cadastrar(self):
        self.nome = input("Digite o nome: ")
        self.limite = float (input("Digite limite: ") )
        self.cnpj = input("Digite o CNPJ: ")

    def __str__(self) -> str:
        return super().__str__() + "\nCNPJ: " + self.cnpj