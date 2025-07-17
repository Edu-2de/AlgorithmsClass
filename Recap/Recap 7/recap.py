class No:
      def __init__(self, valor):
            self.valor = valor         # Valor armazenado no nó
            self.proximo = None        # Referência para o próximo nó (inicia vazio)

class ListaEncadeada:
      def __init__(self):
            self.inicio = None        # Referência para o primeiro nó da lista

      def adicionar(self, valor):
            novo_no = No(valor)       # Cria um novo nó com o valor dado
            if not self.inicio:       # Se a lista está vazia
                  self.inicio = novo_no   # O novo nó vira o início da lista
            else:
                  atual = self.inicio     # Começa do início
                  while atual.proximo:    # Percorre até o último nó
                        atual = atual.proximo
                  atual.proximo = novo_no # Adiciona o novo nó ao final

      def exibir(self):
            atual = self.inicio           # Começa do início
            while atual:                  # Enquanto houver nós
                  print(atual.valor, end=" -> ")  # Mostra o valor do nó
                  atual = atual.proximo           # Vai para o próximo nó
            print("None")                 # Indica o fim da lista

      def remover(self, valor):
            if not self.inicio:           # Se a lista está vazia, não faz nada
                  return

            if self.inicio.valor == valor:    # Se o valor está no início
                  self.inicio = self.inicio.proximo  # Remove o primeiro nó
                  return

            atual = self.inicio
            # Procura o nó anterior ao que deve ser removido
            while atual.proximo and atual.proximo.valor != valor:
                  atual = atual.proximo

            if atual.proximo:              # Se encontrou o valor
                  atual.proximo = atual.proximo.proximo  # Remove o nó da lista