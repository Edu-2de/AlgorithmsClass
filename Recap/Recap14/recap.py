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
    
class NoLivro:
    def __init__(self, livro):
        self.livro = livro
        self.proximo = None

class ListaLivro:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    def adicionar(self, valor ):
        if self.inicio:
            aux = self.inicio
            while( aux.proximo ):
                aux = aux.proximo
            aux.proximo = NoLivro( valor )
        else:
            self.inicio = NoLivro( valor )
        self.tamanho = self.tamanho + 1

    def imprimir(self):
        if self.inicio == None:
            print("Lista Vazia")

            aux = self.inicio
            while( aux ):
                print( aux.livro , "\n" )
                aux = aux.proximo
                print( "Tamanho da Lista: " + str(self.tamanho ))

    def exculir(self, valor):
        if self.tamanho == 0:
            print("A lista esta vazia")
        elif self.tamanho == 1:
            if self.inicio.livro == valor:
                self.inicio = None
                self.tamnho -= 1
            else:
                print("Valor nao encontrado")
        else:
            aux = self.inicio
            if self.inicio.livro == valor:
                aux = self.inicio.proximo
                self.inicio = aux
                self.tamanho -= 1
            else:
                ant = self.inicio
                aux = ant.proximo
                while (aux):
                    if aux.livro == valor:
                        ant.proximo = aux.proximo
                        self.tamanho -= 1
                    else:
                        ant = aux
                    aux = aux.proximo
    