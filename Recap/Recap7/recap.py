class No:
      def __init__(self, valor):
            self.valor = valor
            self.proximo = None

class ListaEncadeada:
      def __init__(self):
            self.inicio = None

      def adicionar(self, valor):
            novo_no = No(valor)
            if not self.inicio:
                  self.inicio = novo_no
            else:
                  atual = self.inicio
                  while atual.proximo:
                        atual = atual.proximo
                  atual.proximo = novo_no

      def exibir(self):
            atual = self.inicio
            while atual:
                  print(atual.valor, end=" -> ")
                  atual = atual.proximo
            print("None")

      def remover(self, valor):
            if not self.inicio:
                  return

            if self.inicio.valor == valor:
                  self.inicio = self.inicio.proximo
                  return

            atual = self.inicio
            while atual.proximo and atual.proximo.valor != valor:
                  atual = atual.proximo

            if atual.proximo:
                  atual.proximo = atual.proximo.proximo

      
