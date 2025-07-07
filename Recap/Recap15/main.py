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
            if pessoanova.idade >= 60:
                if self.inicio.pessoa.idade < 60:
                    x = NoPessoa(pessoanova)
                    x.proximo = aux
                    self.inicio = x
                    return "\nA pessoa prioritaria foi adicionada no comeco da fila"
                
                elif self.inicio.pessoa.idade >=60:
                    while aux.proximo and aux.proximo.pessoa.idade >= 60:
                        aux = aux.proximo
                    x = NoPessoa(pessoanova)
                    x.proximo = aux.proximo
                    aux.proximo = x
                 
                    print(f"\nA pessoa prioritaria foi adicionada a fila, conforme sua idade")

              
            else:
                while(aux.proximo):
                    aux = aux.proximo
                aux.proximo = NoPessoa(pessoanova)
                print(f"\nA pessoa foi adicionada no final da fila")
                
        else:
            self.inicio = NoPessoa(pessoanova)
            print("\nA pessoa foi adicionada no comeco da fila")
        self.tamanho  += 1


    def chamarProximo(self):
        if self.inicio:
            aux = self.inicio
            print (f"{aux.pessoa}, é sua vez!")
            self.inicio = self.inicio.proximo
            self.tamanho -= 1
        else:
            print('A lista esta vazia, nao ha mais ninguem para chamar!')


    def imprimir(self):
        if self.inicio == None:
            print("\nA lista esta vazia!")
        
        aux = self.inicio
        contador = 0
        print("\n============= FILA =============\n")
        while (aux):
            contador += 1
            print(  f"{contador}. {aux.pessoa.nome}{aux.pessoa.idade} anos e senha: {aux.pessoa.senha}" )
            aux = aux.proximo


    def buscar(self,senha_digitada):
        if self.inicio:
            aux = self.inicio
            while(aux and aux.pessoa.senha != senha_digitada):
                aux = aux.proximo
            if aux != None:
                print(aux.pessoa)
            else:
                print("\nSenha nao encontrada!")
        else:
            print("\nA fila esta vazia")


    def removerPelaSenha(self, senha_digitada):
        if self.inicio:
            anterior = None
            atual = self.inicio
                
            while(atual and atual.pessoa.senha != senha_digitada):
                anterior = atual
                atual = atual.proximo

            if atual == self.inicio:
                self.inicio = self.inicio.proximo
                self.tamanho -= 1
                print(f"\nPessoa: {atual.pessoa} foi removido(a) com sucesso!")

            elif atual != None:
                anterior.proximo = atual.proximo
                self.tamanho -= 1
                print(f"\nPessoa: {atual.pessoa} foi removido(a) com sucesso!")

            else: 
                print("\nSenha nao encontrada!")
        else:
            print("\nA fila esta vazia")



 
        

lista = ListaPessoa()
def menu():
    while True:
        print("\n============= MENU =============")
        print("1. Inserir na fila")
        print("2. Chamar proxima pessoa")
        print("3. Listar fila")
        print("4. Buscar pessoa pela senha")
        print("5. Remover pessoa pela senha")
        print("6. Sair")
        print("================================")
        
        opcao = input("\nDigite a opcao que deseja: ")
        if opcao == "1":
            print("\n====OPCAO ESCOLHIDA: 1.Inserir na fila====")

            nome = input("\nDigite seu nome: ")
            idade = int(input("Digite sua idade: "))
    
            pessoa = Pessoa(nome, idade)

            print(pessoa)
            print(f"\n {lista.adicionar(pessoa)}")
        elif opcao == "2":
            print("\n====OPCAO ESCOLHIDA: 2.Chamar proxima pessoa====")

            lista.chamarProximo()
        elif opcao == "3":
            print("\n====OPCAO ESCOLHIDA: 3.Listar fila====")

            lista.imprimir()
        elif opcao == "4":
            print("\n====OPCAO ESCOLHIDA: 4.Buscar pessoa pela senha====")

            senha = input("\nDigite a senha que deseja buscar: ")
            lista.buscar(senha)
        elif opcao == "5":
            print("\n====OPCAO ESCOLHIDA: 5. Remover pessoa pela senha====")


            senha = input("\nDigite a senha que deseja remover: ")
            lista.removerPelaSenha(senha)
        elif opcao == "6":
            print("\n====voce escolheu: 6. Sair====")
            break
        else:
            print("\nDigite somente opcoes validas!")




        

if __name__ == "__main__":
    menu()
