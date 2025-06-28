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
