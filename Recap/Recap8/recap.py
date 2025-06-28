# Exemplo de lista duplamente encadeada

class No:
    def __init__(self, valor):
        self.valor = valor      # Valor armazenado no nó
        self.proximo = None     # Referência para o próximo nó
        self.anterior = None    # Referência para o nó anterior

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.inicio = None     # Primeiro nó da lista
        self.fim = None        # Último nó da lista

    def adicionar(self, valor):
        novo_no = No(valor)
        if not self.inicio:    # Lista vazia
            self.inicio = novo_no
            self.fim = novo_no
        else:
            self.fim.proximo = novo_no
            novo_no.anterior = self.fim
            self.fim = novo_no

    def exibir(self):
        atual = self.inicio
        while atual:
            print(atual.valor, end=" <-> ")
            atual = atual.proximo
        print("None")

    def exibir_reverso(self):
        atual = self.fim
        while atual:
            print(atual.valor, end=" <-> ")
            atual = atual.anterior
        print("None")

    def remover(self, valor):
        atual = self.inicio
        while atual:
            if atual.valor == valor:
                if atual.anterior:
                    atual.anterior.proximo = atual.proximo
                else:
                    self.inicio = atual.proximo
                if atual.proximo:
                    atual.proximo.anterior = atual.anterior
                else:
                    self.fim = atual.anterior
                return
            atual = atual.proximo

# Exemplo de uso:
lista = ListaDuplamenteEncadeada()
lista.adicionar(1)
lista.adicionar(2)
lista.adicionar(3)
lista.exibir()           # Saída: 1 <-> 2 <-> 3 <-> None
lista.exibir_reverso()   # Saída: 3 <-> 2 <-> 1 <-> None
lista.remover(2)
lista.exibir()           # Saída: 1 <-> 3 <-> None