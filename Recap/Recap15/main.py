import random
import string

'''
Exercício: Gerenciamento de Fila de Atendimento Prioritário

Implemente um sistema de fila de atendimento usando lista encadeada, com as seguintes regras:

Crie uma classe Pessoa com os atributos: nome, idade, e senha (gerada automaticamente).
Implemente uma lista encadeada para representar a fila.
Pessoas com idade maior ou igual a 60 anos devem ser inseridas antes das pessoas não prioritárias, mas depois de outras pessoas prioritárias já na fila.
Implemente métodos para:
Adicionar uma pessoa à fila (respeitando a prioridade)
Chamar (remover) a próxima pessoa da fila
Listar todas as pessoas na fila (em ordem)
Buscar uma pessoa pela senha
Remover uma pessoa da fila pela senha (caso desista do atendimento)
Crie um menu para:
Adicionar pessoa à fila
Chamar próxima pessoa
Listar fila
Buscar pessoa pela senha
Remover pessoa pela senha
Sair
'''

class Pessoa:
    def __init__(self, nome:str = None, idade:int = 0):
        self.nome = nome
        self.idade = idade
        self.senha = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))