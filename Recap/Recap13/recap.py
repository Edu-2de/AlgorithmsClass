import random
import string

class Conta:
    _contador_id = 0
  
    def __init__(self, _saldo:float = 0.0, titular:str = None):
        self.id = Conta._contador_id
        Conta._contador_id += 1
        self.__numero_conta =  ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        self._saldo = _saldo
        self.titular = titular

    def __str__(self):
        return f"A conta: {self.__numero_conta} do titular: {self.titular} foi criada com sucesso"
    
    def sacar(self, valor:float):
        if valor <= self._saldo:
            print(f"Voce sacou: {valor} da sua conta, agora voce tem: {self._saldo} de saldo restante")
