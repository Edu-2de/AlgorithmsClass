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
        while chances:
            try:
                if senha == self.senha:
                    if valor <= self._saldo:
                        self._saldo -= valor
                        print(f"Voce sacou: {valor} da sua conta, agora voce tem: {self._saldo} de saldo restante")
                        break
                    else:
                        print(f"Voce nao tem saldo suficiente para sacar essa quantia")
                        break
                else:
                    chances -= 1
                    print(f"Voce digitou a senha errada, tente novamente, voce ainda tem {chances} chances restantes")

            except:
                print(f"Voce perdeu todas as tentativas tente novamente")
                break

    def depositar(self, valor:float):
        if valor > 0.0:
            self._saldo += valor
            print(f"Voce acaba de depositar {valor} na sua conta, agora voce tem {self._saldo} de saldo")
        else:
            print("Voce so pode depositar uma quantia que seja maior que zero")


    def get_numero_conta(self):
        print(self.__numero_conta)

    def set_numero_conta(self, valor:str, senha:str):
        chances = 3
        while chances:
            try:
                if senha == self.senha:
                    if valor == self.__numero_conta:
                        print("Voce deve digitar um numero de conta diferente da sua atual.")
                        break
                    else:
                        self.__numero_conta = valor
                        print(f"Agora sua conta se indentifica com o numero {valor}")
                        break
                else:
                    chances -= 1
                    print(f"Voce digitou a senha errada, tente novamente, voce ainda tem {chances} chances restantes")
            except:
                print(f"Voce perdeu todas as tentativas tente novamente")
                break



    
