from Cliente import Cliente

class Fisico( Cliente ):

    def __init__(self, nome = None, cpf = None):
        super().__init__(nome)
        self.cpf = cpf

    def cadastrar(self):
        self.nome = input("Digite o nome: ")
        self.limite = float (input("Digite limite: ") )
        self.cpf = input("Digite o CPF: ")

    def __str__(self) -> str:
        return super().__str__() + "\nCPF: " + self.cpf

    

