from No import No

class ListaEncadeadaOrdenada:

    def __init__(self):
        self.inicio = None

    def add(self, valor):
        nodo = No( valor )
        if self.inicio == None:
            self.inicio = nodo
        elif valor < self.inicio.dado:
            nodo.prox = self.inicio
            self.inicio = nodo
        else: 
            ant = self.inicio
            aux = self.inicio.prox
            while aux:
                if valor < aux.dado:
                    ant.prox = nodo
                    nodo.prox = aux
                    break
                else:
                    ant = aux
                    aux = aux.prox
            if aux == None:
                ant.prox = nodo
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

    def remove(self, valor):
        removeu = False
        if self.inicio is not None:
            if valor == self.inicio.dado:
                self.inicio = self.inicio.prox
                removeu = True
            else:
                ant = self.inicio
                aux = self.inicio.prox
                while aux: 
                    if valor == aux.dado:
                        ant.prox = aux.prox
                        removeu = True
                        break
                    else:
                        ant = aux
                        aux = aux.prox
            if removeu:
                print("Elemento ", valor, " removido")
            else: 
                print("Elemento ", valor, " não encontrado")

        self.imprimir()
        


