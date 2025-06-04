class Cidade:

    def __init__(self, nome = "Tangamandápio"):
        self.id = None
        self.nome = nome

    def __str__(self):
        return "Id: " + str( self.id ) + " - Nome da Cidade: " + self.nome

