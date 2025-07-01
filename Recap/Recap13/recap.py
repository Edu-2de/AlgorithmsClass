class Conta:
    _contador_id = 0
    def __init__(self, _saldo:float = 0.0, __numero_conta:str = None, titular:str = None)
        self.id = Conta._contador_id
        Conta._contador_id += 1
        self.__numero_conta = __numero_conta
        self.titular = titular

    def