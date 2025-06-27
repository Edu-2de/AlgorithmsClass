from Autor import Autor
from Livro import Livro

class NodoAutor:
    def __init__(self, autor):
        self.autor = autor
        self.proximo = None

class ListaAutores:
    def __init__(self):
        self.cabeca = None

    def inserir_ordenado(self, autor):
        novo_nodo = NodoAutor(autor)
        if self.cabeca is None or autor.nome < self.cabeca.autor.nome:
            novo_nodo.proximo = self.cabeca
            self.cabeca = novo_nodo
            return
        atual = self.cabeca
        while atual.proximo and atual.proximo.autor.nome < autor.nome:
            atual = atual.proximo
        novo_nodo.proximo = atual.proximo
        atual.proximo = novo_nodo

    def listar_autores(self):
        autores = []
        atual = self.cabeca
        while atual:
            autores.append(atual.autor)
            atual = atual.proximo
        return autores

def menu():
    lista_autores = ListaAutores()
    while True:
        print("\n--- MENU BIBLIOTECA ---")
        print("1. Cadastrar autor")
        print("2. Listar autores")
        print("3. Adicionar livro a um autor")
        print("4. Listar livros de um autor")
        print("5. Remover livro de um autor")
        print("6. Sair")
        opc = input("Escolha uma opção: ")

        if opc == '1':
            nome = input("Nome do autor: ")
            nac = input("Nacionalidade: ")
            autor = Autor(nome=nome, nacionalidade=nac)
            lista_autores.inserir_ordenado(autor)
            print("Autor cadastrado com sucesso.")
        elif opc == '2':
            autores = lista_autores.listar_autores()
            if not autores:
                print("Nenhum autor cadastrado.")
            for idx, autor in enumerate(autores, 1):
                print(f"{idx}. {autor}")
        elif opc == '3':
            autores = lista_autores.listar_autores()
            if not autores:
                print("Nenhum autor cadastrado.")
                continue
            for idx, autor in enumerate(autores, 1):
                print(f"{idx}. {autor.nome}")
            try:
                idx_autor = int(input("Escolha o número do autor: ")) - 1
                autor_sel = autores[idx_autor]
            except (ValueError, IndexError):
                print("Autor inválido.")
                continue
            titulo = input("Título do livro: ")
            paginas = int(input("Número de páginas: "))
            livro = Livro(titulo=titulo, autor=autor_sel, paginas=paginas)
            print(f"Livro '{titulo}' adicionado ao autor {autor_sel.nome}.")
        elif opc == '4':
            autores = lista_autores.listar_autores()
            if not autores:
                print("Nenhum autor cadastrado.")
                continue
            for idx, autor in enumerate(autores, 1):
                print(f"{idx}. {autor.nome}")
            try:
                idx_autor = int(input("Escolha o número do autor: ")) - 1
                autor_sel = autores[idx_autor]
            except (ValueError, IndexError):
                print("Autor inválido.")
                continue
            if not autor_sel.livros:
                print("Autor não possui livros.")
            else:
                for idx, livro in enumerate(autor_sel.livros, 1):
                    print(f"{idx}. {livro.titulo} - {livro.paginas} páginas")
        elif opc == '5':
            autores = lista_autores.listar_autores()
            if not autores:
                print("Nenhum autor cadastrado.")
                continue
            for idx, autor in enumerate(autores, 1):
                print(f"{idx}. {autor.nome}")
            try:
                idx_autor = int(input("Escolha o número do autor: ")) - 1
                autor_sel = autores[idx_autor]
            except (ValueError, IndexError):
                print("Autor inválido.")
                continue
            if not autor_sel.livros:
                print("Autor não possui livros.")
                continue
            for idx, livro in enumerate(autor_sel.livros, 1):
                print(f"{idx}. {livro.titulo}")
            try:
                idx_livro = int(input("Escolha o número do livro para remover: ")) - 1
                livro_removido = autor_sel.livros.pop(idx_livro)
                print(f"Livro '{livro_removido.titulo}' removido.")
            except (ValueError, IndexError):
                print("Livro inválido.")
        elif opc == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()