from Categoria import Categoria
from Produto import Produto

class Estoque:
      def __init__(self):
            self.produtos = []
            self.categorias = []

      
      def adicionar_produto(self, produto:Produto):
            if isinstance(produto, Produto):
                  self.produtos.append(produto)
            else:
                  raise TypeError("Produto deve ser uma instância de Produto")
      
      def adicionar_categoria(self, categoria:Categoria):
            if isinstance(categoria, Categoria):
                  self.categorias.append(categoria)
            else:
                  raise TypeError("Categoria deve ser uma instância de Categoria")
            

      def remover_produto(self, produto:Produto):
            if isinstance(produto, Produto) and produto in self.produtos:
                  self.produtos.remove(produto)
            else:
                  raise ValueError("Produto não está registrado no estoque")

      def remover_categoria(self, categoria:Categoria):
            if isinstance(categoria, Categoria) and categoria in self.categorias:
                  self.categorias.remove(categoria)
            else:
                  raise ValueError("Categoria não está registrada no estoque")
            

            
      def adicionar_categoria_a_produto(self, produto:Produto, categoria:Categoria):
            if produto in self.produtos and categoria in self.categorias:
                  produto.adicionar_categoria(categoria)
            else:
                  raise ValueError("Produto ou categoria não estão registrados no estoque")
            
      def remover_categoria_de_produto(self, produto:Produto, categoria:Categoria):
            if produto in self.produtos and categoria in self.categorias and categoria in produto.categorias:
                  produto.remover_categoria(categoria)
            else:
                  raise ValueError("Produto ou categoria não estão registrados no estoque ou a categoria não está associada ao produto")
            

      def listar_categorias_de_produto(self, produto:Produto):
            if produto in self.produtos:
                  return produto.categorias
            else:
                  raise ValueError("Produto não está registrado no estoque")
            
      def listar_produtos_de_categoria(self, categoria:Categoria):
            if categoria in self.categorias:
                  return categoria.produtos
            else:
                  raise ValueError("Categoria não está registrada no estoque")
            

      def listar_produtos(self):
            return self.produtos
      
      def listar_categorias(self):
            return self.categorias
      

      def listar_informacoes_produto(self, produto:Produto):
            if produto in self.produtos:
                  return str(produto)
            else:
                  raise ValueError("Produto não está registrado no estoque")
            
      def listar_informacoes_categoria(self, categoria:Categoria):
            if categoria in self.categorias:
                  return str(categoria)
            else:
                  raise ValueError("Categoria não está registrada no estoque")
            

      def __str__(self):
            produtos_info = "\n".join([str(produto) for produto in self.produtos]) if self.produtos else "Nenhum produto no estoque"
            categorias_info = "\n".join([str(categoria) for categoria in self.categorias]) if self.categorias else "Nenhuma categoria no estoque"
            return f"Estoque:\nProdutos:\n{produtos_info}\n\nCategorias:\n{categorias_info}"
      

      

            
      
      