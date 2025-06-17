class Autor:
    def __init__(self, id: int = 0, nome: str = None, nacionalidade: str = None):
        self.id = id + 1
        self.nome = nome
        self.nacionalidade = nacionalidade
        self.livros = []
        self._validar() 

    def _validar(self):
        if self.nome is not None and not isinstance(self.nome, str):
            raise TypeError("nome deve ser uma string")
        if self.nacionalidade is not None and not isinstance(self.nacionalidade, str):
            raise TypeError("nacionalidade deve ser uma string")

    def remover(self):
        if len(self.livros) != 0:
            return self.livros.pop();
        raise TypeError("Nao há itens na lista para remover")

    def adicionar(self, livronovo):
        self.livros.append(livronovo);
        return f"{livronovo} adicionado a lista com sucesso na ultima posicao, {self.livros}"   

    def removercomposicao(self, id):
        temporarios = []
        while self.livros:
            livro = self.livros.pop()  
            if livro.id == id:
                break 
            else:
                temporarios.append(livro)

    def __str__(self):
        return f"nome: {self.nome}\nnacionalidade: {self.nacionalidade}"


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
            novo_nodo.proximo = self.cabeca #essa linha define o primeiro elemento da lista basicamente
                                            # Faz o novo nó apontar para o antigo primeiro elemento (cabeça da lista)

            self.cabeca = novo_nodo# e essa define que o cabeca equivale ao primeiro elento da lista
                                   # Atualiza a cabeça para que ela aponte para o novo nó (agora o primeiro da lista)

            return
  
        atual = self.cabeca
        while atual.proximo and atual.proximo.autor.nome < autor.nome:
            atual = atual.proximo
        novo_nodo.proximo = atual.proximo
        atual.proximo = novo_nodo