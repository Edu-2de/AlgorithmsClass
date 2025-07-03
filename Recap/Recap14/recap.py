import random
import string


class Livro:
    _contador_id = 0
    def __init__(self, titulo:str = None, autor:str = None, ano:int = 0000):
        self.id = Livro._contador_id
        Livro._contador_id += 1
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.codigo =  ''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) 