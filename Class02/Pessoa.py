from Cidade import Cidade

class Pessoa:
    def __init__(self, nome = None, cpf = None, cid = Cidade("Itati") ):
        self.id = None
        self.nome = nome
        self.cpf = cpf
        self.cidade = cid
        self.salario = 1518.00

    def setSalario(self, valor ):
        if valor > self.salario:
            self.salario = valor

    def __str__(self):
        txt = "Nome: " + self.nome 
        txt += "\nCPF: " + str( self.cpf ) 
        txt += "\nSalário: " + str( self.salario )
        #txt += "\nCidade: " + self.cidade.nome
        txt += "\nCidade: " + str( self.cidade )
        return txt
        

    


    