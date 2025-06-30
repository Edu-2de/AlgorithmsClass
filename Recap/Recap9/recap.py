class No:
      def __init__(self, valor):
            self.valor = valor      # Valor armazenado no nó
            self.proximo = None


class Fila:

      def __init__(self):
            self.primeiro = None  # Referência para o primeiro nó
            self.ultimo = None        # Referência para o último nó
            self.tamanho = 0          # Tamanho da fila

      def enfileirar(self, valor):
            novo_no = No(valor)
            if self.tamanho == 0:
                  self.primeiro = novo_no
                  self.ultimo = novo_no
            else:
                  self.ultimo.proximo = novo_no
                  self.ultimo = novo_no
            self.tamanho += 1

      def desenfileirar(self):
            if self.tamanho == 0:
                  return None
            valor = self.primeiro.valor
            self.primeiro = self.primeiro.proximo
            self.tamanho -= 1
            if self.tamanho == 0:
                  self.ultimo = None
            return valor

      def tamanho(self):
            return self.tamanho
      
      def imprimir(self):
            atual = self.primeiro
            while atual:
                  print(atual.valor, end=" -> ")
                  atual = atual.proximo
            print("None")

      def adicionar(self, valor):
            self.enfileirar(valor)

      def remover(self):
            return self.desenfileirar()