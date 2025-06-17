from Autor import Autor


class Livro:
    def __init__(self, titulo:str=None, autor:Autor=None, paginas:int=0):
        self.titulo = titulo
        self.autor = autor   
        self.paginas = paginas
        self.livros = autor.livros.append(self) 

   

    def __str__(self):
        return f"titulo: {self.titulo}\nnacionalidade: {self.autor}\npaginas: {self.paginas}"