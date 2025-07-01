import random
import string

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
    
    def marcarPresenca(self) -> None:
        print(f"{self.nome} esta presente")

    def matricular(self) -> None:
        print(f"Matricula sendo realizada se a pessoa for um aluno")

    
class Aluno(Pessoa):
    def __init__(self, id:int = 0, nome:str = None, _cpf:str = None, __matricula:str = None):
        super().__init__(id, nome, _cpf),
        self.__matricula = __matricula

    def __str__(self):
        return f"Aluno do id: {self.id}, nome: {self.nome}, cpf: {self._cpf} e matricula: {self.__matricula} foi adicionado(a) com sucesso"
    
    def marcarPresenca(self) -> None:
        super().marcarPresenca()

    
    def  matricular(self) -> str:
        super().matricular()
        tamanho = 8
        aleatorio = ''.join(random.choices(string.ascii_letters + string.digits, k=tamanho))
        self.__matricula = aleatorio
        return f"Aluno {self.nome} cadastrado com sucesso de matricula: {self.__matricula}"
    
    
    

      



 
