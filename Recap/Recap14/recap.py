import random
import string

'''
Crie um sistema de gerenciamento de biblioteca usando **lista encadeada** para armazenar os livros.

Requisitos:

- Crie uma classe Livro com os atributos: título, autor, ano e código (gerado automaticamente).
- Implemente uma lista encadeada para armazenar os livros (cada nó deve conter um Livro).
- Implemente métodos para:
    - Adicionar um novo livro à lista (no início ou no final).
    - Remover um livro pelo código.
    - Buscar um livro pelo título.
    - Listar todos os livros cadastrados.
- Crie um menu para:
    - Adicionar livro
    - Remover livro
    - Buscar livro
    - Listar todos os livros
    - Sair

Dica: Não use listas Python para armazenar os livros, use apenas a estrutura de lista encadeada que você criar!
'''
class Livro:
    _contador_id = 0
    def __init__(self, titulo:str = None, autor:str = None, ano:int = 0000):
        self.id = Livro._contador_id
        Livro._contador_id += 1
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.codigo =  ''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) 

    def __str__(self):
        return f"Livro: {self.titulo}, do autor: {self.autor}, do ano: {self.ano} e codigo {self.codigo}"