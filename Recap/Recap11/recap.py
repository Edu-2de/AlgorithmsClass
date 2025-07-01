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
      def __init__(self, id:int = 0, nome:str = None, cpf:str = None):
            self.id = id + 1,

 
