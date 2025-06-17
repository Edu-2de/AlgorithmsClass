from Produto import Produto

class Categoria:
      def __init__(self, nome:str = None, descricao:str = None):
            self.nome = nome
            self.descricao = descricao
            self.produtos = []
      
      def __str__(self):
            return f"Categoria: {self.nome}\n descricao: {self.descricao} \n Produtos: {', '.join([produto.nome for produto in self.produtos]) if self.produtos else "Nenhum produto"}"
      
      def adicionar_produto(self, produto:Produto):
            if produto:
                  self.produtos.append(produto)
                  produto.categorias.append(self)
            else:
                  raise TypeError("Produto deve ser uma instância de Produto")
      
      def remover_produto(self, produto:Produto):
            if produto in self.produtos:
                  self.produtos.remove(produto)
                  produto.categorias.remove(self)
            else:
                  raise TypeError("Este produto não possui uma categoria para remover")