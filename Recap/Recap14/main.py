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

    def adicionar_comeco(self, valor):
        if self.inicio:
            novoinicio = NoLivro(valor)
            novoinicio.proximo = self.inicio
            self.inicio = novoinicio
            self.tamanho += 1
            print("O livro foi adicionado no comeco da lista!")
        else:
            self.inicio = NoLivro( valor )
            self.tamanho += 1
            print("O livro foi adicionado no comeco da lista!")

    def adicionar(self, valor ):
        if self.inicio:
            aux = self.inicio
            while( aux.proximo ):
                aux = aux.proximo
            aux.proximo = NoLivro( valor )
            print("O livro foi adicionado no final da lista!")
        else:
            self.inicio = NoLivro( valor )
            print("O livro foi adicionado no comeco da lista! (porque ela estava vazia)")
        self.tamanho = self.tamanho + 1

    def imprimir(self):
        if self.inicio == None:
            print("Lista Vazia")

        aux = self.inicio
        while( aux ):
            print(  "\n", aux.livro , "\n" )
            aux = aux.proximo
        print( "Tamanho da Lista: " + str(self.tamanho ))

    def exculir(self, valor):
        if self.tamanho == 0:
            print("A lista esta vazia")
        elif self.tamanho == 1:
            if self.inicio.livro.codigo == valor:
                self.inicio = None
                self.tamnho -= 1
            else:
                print("Valor nao encontrado")
        else:
            aux = self.inicio
            if self.inicio.livro.codigo == valor:
                aux = self.inicio.proximo
                self.inicio = aux
                self.tamanho -= 1
                print("Livro excluido com sucesso!")
            else:
                ant = self.inicio
                aux = ant.proximo
                while (aux):
                    if aux.livro.codigo == valor:
                        ant.proximo = aux.proximo
                        self.tamanho -= 1
                    else:
                        ant = aux
                    aux = aux.proximo
                    print("Livro excluido com sucesso!")


    def buscar(self, valor):
        if self.tamanho == 0:
            print("A lista esta vazia")
        elif self.tamanho == 1:
            if self.inicio.livro.titulo == valor or self.inicio.livro.codigo == valor:
                print(self.inicio.livro)
            else:
                print("Esse livro nao esta na lista!")
        else: 
            ant = self.inicio
            aux = ant.proximo
            while (aux):
                if aux.livro.titulo == valor or aux.livro.codigo == valor:
                    print(aux.livro)
                else:
                    ant = aux
                aux = aux.proximo
                    
            



lista = ListaLivro()
def menu():
    while True:
            print("\n--- livros ---")   
            print("1. Cadastrar livro")
            print("2. Remover livro")
            print("3. Buscar livro")
            print("4. Listar todos os livros")
            print("5. Sair")
            opcao_escolhida = input("Digite a opcao que deseja: ")
          
            if opcao_escolhida == "1":
                print("\nVoce escolheu: Cadastrar livro ")
                titulo = input("Qual o titulo do livro? ")
                autor = input(f"Qual o autor de {titulo}? ")  
                ano = input(f"Qual o ano em que {titulo} foi lancado? ")
                livro = Livro(titulo, autor, ano)
                print(f"\n{livro}")
                
                final_ou_comeco = input("\nVoce deseja adicionar esse livro no comeco ou no final da lista? ")
                if final_ou_comeco == "comeco":
                    lista.adicionar_comeco(livro)
                    print(f"O livro {titulo} foi adicionado no comeco da lista!")
             
                elif final_ou_comeco == "final":
                    lista.adicionar(livro)
                    print(f"O livro {titulo} foi adicionado no final da lista!")
              
                else:
                    print("Digite somente comeco ou final (desse jeito)")
            elif opcao_escolhida == "2":
                print("\nVoce escolheu: Remover livro ")
                codigo = input("Qual o codigo do livro que voce deseja remover? ")
                lista.exculir(codigo)
            elif opcao_escolhida == "3":
                titulo_ou_codigo = input("Digite o titulo ou codigo do livro que deseja ver: ")
                lista.buscar(titulo_ou_codigo)
            elif opcao_escolhida == "4":
                lista.imprimir()

            elif opcao_escolhida == "5":
                break






if __name__ == "__main__":
    menu()
