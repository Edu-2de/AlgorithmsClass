from abc import ABC, abstractmethod

class Cliente( ABC ):

    def __init__(self, nome):
        self.nome = nome
        self.__limite = 0.0

    def __str__(self) -> str:
        return "Nome: "+self.nome+"\nLimite: "+self.__limite

    def imprimir(self):
        print( self )
    
    @abstractmethod
    def cadastrar(self):
        pass

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor):
        if valor > self.__limite:
            self.__limite = valor