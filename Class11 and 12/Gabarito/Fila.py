from Carro import Carro

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def add(self, car):
        if self.inicio == None:
            self.inicio = car
        elif self.inicio.prox is None:
            self.inicio.prox = car
        else:
            aux = self.inicio
            while aux.prox:
                aux = aux.prox
            aux.prox = car
        self.fim = car
        self.imprimir()

    def imprimir(self):
        print( "--------Fila de Carros -------------")
        if self.inicio == None:
            print( "Fila vazia!")
        else:
            aux = self.inicio
            txt = ""
            while aux != None:
                txt += str(aux) + " | " 
                aux = aux.prox
            print( txt )
    
    def lavar(self):
        if self.inicio is not None:
            car = self.inicio
            self.inicio = self.inicio.prox
            if self.inicio == None:
                self.fim = None
            print( car.modelo, " - ", car.placa, ", foi lavado")
        self.imprimir()