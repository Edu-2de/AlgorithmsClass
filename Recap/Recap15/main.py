

class Pessoa:
    def __init__(self, nome:str = None, idade:int = 0):
        self.nome = nome
        self.idade = idade
        self.senha = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))