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
    
    def mover(self) -> None:
        print(f"O Veiculo esta se movendo") 
    

class Carro(Veiculo):
    def __init__(self, id:int = 0, marca:str = None, modelo:str = None, __placa:str = None):
        super().__init__(id, marca, modelo)
        self.__placa = __placa

    def __str__(self):
        return f"Carro da placa: {self.__placa} cadastrado com sucesso"
    
    def mover(self) -> str:
        super().mover()
        return f"O carro está dirigindo"
    

class Bicicleta(Veiculo):
    def __init__(self, id:int = 0, marca:str = None, modelo:str = None, _marchas:int = 0, marcha_atual:int = 0, velocidade_atual:float = 0.0):
        super().__init__(id, marca, modelo)
        self._marchas = _marchas,
        self.marcha_atual = marcha_atual,
        self.velocidade_atual = velocidade_atual

    def __str__(self):
        return f"Bicicleta de {self._marchas} foi cadastrada com sucesso"
    
    def mover(self) -> str:
        super().mover()
        self.velocidade_atual += 1.5
        return f"A bicicleta está pedalando "
    
    def acelerar(self, velocidade:float) -> str:
        if velocidade < self.velocidade_atual and velocidade > 0.0:
            self.marcha_atual -= 1
            self.velocidade_atual = velocidade
            return(f"A bicicleta diminuiu uma mrcha e agora esta com a veolocidade de: {self.velocidade_atual} km")
        elif velocidade > self.velocidade_atual:
            self.marcha_atual += 1
            self.velocidade_atual = velocidade
            return(f"A bicicleta aumentou uma mrcha e agora esta com a veolocidade de: {self.velocidade_atual} km")
        else:
            return(f"A bicicleta já está parada, voce nao pode diminuir a marcha")




