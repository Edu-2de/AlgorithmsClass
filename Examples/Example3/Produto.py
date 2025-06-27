from Categoria import Categoria

class Produto:
      def __init__(self, nome:str = None, preco:float = 0.0, quantidade:int = 0, codigo:str = None, descricao:str = None):
            self.nome = nome
            self.preco = preco
            self.quantidade = quantidade
            self.codigo = codigo
            self.descricao = descricao
            self.categorias = []

      def __str__(self):
            return f"Produto: {self.nome}\nPreço: {self.preco}\nQuantidade: {self.quantidade}\nCódigo: {self.codigo}\nDescrição: {self.descricao}\nCategorias: {', '.join([categoria.nome for categoria in self.categorias]) if self.categorias else 'Nenhuma categoria'}"

      def adicionar_categoria(self, categoria:Categoria):
            if categoria:
                  self.categorias.append(categoria)
                  categoria.produtos.append(self)
            else:
                  raise TypeError("Categoria deve ser uma instância de Categoria")

      def remover_categoria(self, categoria:Categoria):
            if categoria in self.categorias:
                  self.categorias.remove(categoria)
                  categoria.produtos.remove(self)
            else:
                  raise TypeError("Este produto não possui uma categoria para remover")