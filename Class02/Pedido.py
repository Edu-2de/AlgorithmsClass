from Produto import Produto
from Pessoa import Pessoa
from datetime import date


class Pedido:

    def __init__(self, data = date.today(), cli = Pessoa("Balcão") ):
        self.id = None
        self.data = data 
        self.cliente = cli
        self.produtos = []

    def addProd( self, prod ):
        if prod :
            self.produtos.append( prod )
        soma = 0.0
        for p in self.produtos:
            soma += p.preco
        return soma 

    def __str__(self):
        txt = "Data: " + str(self.data)
        txt += "\n" + str( self.cliente )
        txt += "\n Produtos: " 
        for p in self.produtos:
            txt += "\nNome do Produto: " + p.nome
            txt += "\nPreço: " + str( p.preco ) 
            txt += "\n---------------------"
        return txt
        

