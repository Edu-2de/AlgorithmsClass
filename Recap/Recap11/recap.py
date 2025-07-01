'''
Construa um algoritmo para implementar o seguinte diagrama de classes:
Requisitos:

- A classe pessoa é abstrata
- O método marcarPresenca da classe pessoa é abstrato
- O atributo cpf é fracamente privado
- O atributo matrícula é fortemente privado

Construa um método assessor e um método modificador para o atributo matrícula
Construa um arquivo main para testar a construção de um aluno
'''

class Pessoa:
    def __init__(self, id:int = 0, nome:str = None, _cpf:str = None):
        self.id = id + 1,
        self.nome = nome,
        self._cpf = _cpf

    def __str__(self):
        return f"Pessoa do id: {self.id}, nome: {self.nome} e de cpf: {self._cpf} foi cadastrada com sucesso"
    
class Aluno(Pessoa):
    def __init__(self, id:int = 0, nome:str = None, _cpf:str = None, __matricula:str = None):
        



 
