''' 
Construa um algoritmo para implementar o seguinte diagrama de classes:

Requisitos:

- Crie uma classe abstrata chamada Veiculo.
- O método mover da classe Veiculo deve ser abstrato.
- Crie as classes Carro e Bicicleta que herdam de Veiculo.
- Ambas devem implementar o método mover de forma diferente (ex: "O carro está dirigindo", "A bicicleta está pedalando").
- O atributo placa do Carro deve ser fortemente privado.
- O atributo marchas da Bicicleta deve ser fracamente privado.
- Implemente métodos assessores (getter) e modificadores (setter) para ambos os atributos privados.
- Crie um arquivo main para testar a criação de um carro e de uma bicicleta, mostrando o funcionamento dos métodos e dos getters/setters.
'''

class Veiculo:
    def __init__(self, id:int = 0, marca:str = None, modelo:str = None):
        self.id = id + 1,
        self.marca = marca, 
        self.modelo = modelo

    def __str__(self):
        return f"Veiculo da marca: {self.marca} e do modelo: {self.modelo} foi criado com sucesso"
    

class Carro(Veiculo):
    def __init__(self, id:int = 0, marca:str = None, modelo:str = None, __placa:str = None):
        super().__init__(id, marca, modelo)
        self.__placa = __placa

    
