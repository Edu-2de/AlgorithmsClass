class Autor:
    def __init__(self, nome: str, nacionalidade: str):
        self.nome = nome
        self.nacionalidade = nacionalidade

class NoAutor:
    def __init__(self, autor: Autor):
        self.autor = autor
        self.proximo = None

class ListaAutores:
    def __init__(self):
        self.inicio = None

    def adicionar(self, autor: Autor):
        novo_no = NoAutor(autor)
        if not self.inicio or autor.nome.lower() < self.inicio.autor.nome.lower():
            novo_no.proximo = self.inicio
            self.inicio = novo_no
        else:
            atual = self.inicio
            while atual.proximo and autor.nome.lower() > atual.proximo.autor.nome.lower():
                atual = atual.proximo
            novo_no.proximo = atual.proximo
            atual.proximo = novo_no

    def imprimir(self):
        atual = self.inicio
        print("Autores:")
        while atual:
            print(f"Nome: {atual.autor.nome}, Nacionalidade: {atual.autor.nacionalidade}")
            atual = atual.proximo

    def buscar(self, nome):
        atual = self.inicio
        while atual:
            if atual.autor.nome.lower() == nome.lower():
                return atual.autor
            atual = atual.proximo
        return None

class Livro:
    def __init__(self, titulo: str, autor: Autor, paginas: int):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

class PilhaLivros:
    def __init__(self):
        self.livros = []

    def adicionar(self, livro: Livro):
        self.livros.append(livro)

    def remover(self):
        if self.livros:
            return self.livros.pop()
        else:
            print("Pilha de livros vazia.")
            return None

    def imprimir(self):
        print("Pilha de Livros (do topo para base):")
        for livro in reversed(self.livros):
            print(f"Título: {livro.titulo}, Autor: {livro.autor.nome}, Páginas: {livro.paginas}")

# Menu principal
autores = ListaAutores()
pilha_livros = PilhaLivros()

while True:
    print("\n--- Menu ---")
    print("1. Adicionar autor")
    print("2. Adicionar livro")
    print("3. Remover livro do topo da pilha")
    print("4. Imprimir lista de autores")
    print("5. Imprimir pilha de livros")
    print("6. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do autor: ")
        nacionalidade = input("Nacionalidade: ")
        autores.adicionar(Autor(nome, nacionalidade))
        print("Autor adicionado com sucesso.")
    elif opcao == "2":
        titulo = input("Título do livro: ")
        nome_autor = input("Nome do autor (deve estar cadastrado): ")
        autor = autores.buscar(nome_autor)
        if not autor:
            print("Autor não encontrado. Cadastre o autor primeiro.")
            continue
        paginas = int(input("Número de páginas: "))
        pilha_livros.adicionar(Livro(titulo, autor, paginas))
        print("Livro adicionado à pilha.")
    elif opcao == "3":
        livro = pilha_livros.remover()
        if livro:
            print(f"Livro removido: {livro.titulo}")
    elif opcao == "4":
        autores.imprimir()
    elif opcao == "5":
        pilha_livros.imprimir()
    elif opcao == "6":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")