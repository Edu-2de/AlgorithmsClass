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

    def __str__(self):
        return f"{self.nome} de {self.idade} anos"
    

class NoPessoa:
    def __init__(self, pessoa):
        self.pessoa = pessoa
        self.proximo = None
        self.anterior = None

class ListaPessoa:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    def adicionar(self, pessoanova):
        if self.inicio:
            aux = self.inicio
            if self.inicio.pessoa.idade < 60 and pessoanova.idade >= 60:
                x = NoPessoa(pessoanova)
                x.proximo = aux
                self.inicio = x
                return x
                
            elif aux.proximo != None and aux.proximo.pessoa.idade >= 60:
                while aux.proximo and aux.proximo.pessoa.idade >= 60:
                    aux = aux.proximo
                    
                aux.proximo = NoPessoa(pessoanova)
            else:  
                while(aux.proximo):
                    aux = aux.proximo
                aux.proximo = NoPessoa(pessoanova)
            print(f"A pessoa foi adicionada a fila, conforme sua idade")
        else:
            self.inicio = NoPessoa(pessoanova)
            print("A pessoa foi adicionada no comeco da fila")
        self.tamanho  += 1

    def imprimir(self):
        if self.tamanho == 0:
            print("A lista esta vazia!")
        
        aux = self.inicio
        while (aux):
            print("\n---- Fila ----")
            print(  "\n", aux.pessoa.nome + " " + aux.pessoa.idade + " anos e senha:"+ " " + aux.pessoa.senha)
            aux = aux.proximo

lista = ListaPessoa()
def menu():
    while True:
        print("\n============= FILA =================")
        print("1. Inserir na fila")
        print("2. Chamar proxima pessoa")
        print("3. Listar fila")
        print("4. Buscar pessoa pela senha")
        print("5. Remover pessoa pela senha")
        print("6. Sair")
        
        opcao = input("\nDigite a opcao que deseja: ")
        if opcao == "1":
            print("\n voce escolheu: 1. Inserir na fila")

            nome = input("\nDigite seu nome: ")
            idade = input("Digite sua idade: ")
            pessoa = Pessoa(nome, idade)
            print(pessoa)
            print(f"\n {lista.adicionar(pessoa)}")
        elif opcao == "3":
            lista.imprimir()

        

if __name__ == "__main__":
    menu()
