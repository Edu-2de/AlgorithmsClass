import random
import string

class Conta:
    _contador_id = 0
  
    def __init__(self, _saldo:float = 0.0, titular:str = None, senha:str = None):
        self.id = Conta._contador_id
        Conta._contador_id += 1
        self.__numero_conta =  ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        self._saldo = _saldo
        self.titular = titular
        self.senha = senha

    def __str__(self):
        return f"A conta: {self.__numero_conta} do titular: {self.titular} foi criada com sucesso"
    
    def sacar(self, valor:float, senha:str):
        chances = 3
        while chances :
            try:
                if senha == self.senha:
                    if valor <= self._saldo:
                        self._saldo -= valor
                        print(f"Voce sacou: {valor} da sua conta, agora voce tem: {self._saldo} de saldo restante")
                    else:
                        print(f"Voce nao tem saldo suficiente para sacar essa quantia")
                else:
                    chances -= 1
                    print(f"Voce digitou a senha errada, tente novamente, voce ainda tem {chances} chances restantes")

            except:
                print(f"Voce perdeu todas as tentativas tente novamente")
