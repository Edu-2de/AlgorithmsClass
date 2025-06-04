from No import No

class ListaEncadeada:

    def __init__(self):
        self.inicio = None

    def addNoInicio(self, valor):
        nodo = No(valor)
        if self.inicio is not None:
            nodo.prox = self.inicio
        self.inicio = nodo
        self.imprimir()

    def addNoFim(self, valor):
        nodo = No(valor)
        if self.inicio == None:
            self.inicio = nodo
        elif self.inicio.prox is None:
            self.inicio.prox = nodo
        else:
            aux = self.inicio
            while aux.prox:
                aux = aux.prox
            aux.prox = nodo
        self.imprimir()

    def imprimir(self):
        print( "-------------------------------")
        if self.inicio == None:
            print( "Lista Encadeada vazia!")
        else:
            aux = self.inicio
            while aux != None:
                print( aux.dado )
                aux = aux.prox
    
    def removerDoInicio(self):
        if self.inicio is not None:
            self.inicio = self.inicio.prox
            print( "Elemento removido")
        self.imprimir()

    def removerDoFim(self):
        if self.inicio is not None:
            if self.inicio.prox == None:
                self.inicio = None
            else:
                ant = self.inicio
                aux = self.inicio.prox
                while aux.prox != None:
                    ant = aux
                    aux = aux.prox
                ant.prox = None
            print( "Elemento removido")
        self.imprimir()


