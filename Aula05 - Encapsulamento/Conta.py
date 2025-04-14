class Conta:

    logado = True
    tarifa = 1.99

    def __init__(self):
        self.__saldo = 0.0

#Methods Get and Set
    def getSaldo(self):
        if not Conta.logado:
            return None
        return self.__saldo

    def setSaldo(self, valor):
        if valor > self.__saldo:
            self.__saldo = valor


    def __descontarTarifa(self):
        self.__saldo -= self.tarifa

    def sacar(self, valor):
        if self.__saldo >= valor + self.tarifa:
            self.__saldo -= valor
            self.__descontarTarifa()
            print("Saque Realizado!")
        return None




#Proprety
    @property
    def saldo(self):
        if not Conta.logado:
            return None
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        if valor > self.__saldo:
            self.__saldo = valor