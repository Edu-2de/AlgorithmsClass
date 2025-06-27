class Categoria:
    def __init__(self, nome = None):
        self.nome = nome      
    def __str__(self):
        return f"Nome:  {self.nome}"