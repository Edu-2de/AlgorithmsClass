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
    _contador_id = 0
    def __init__(self, marca:str = None, modelo:str = None):
        self.id = Veiculo._contador_id 
        Veiculo._contador_id += 1  
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return f"Veiculo da marca: {self.marca} e do modelo: {self.modelo} foi criado com sucesso"
    
    def mover(self) -> None:
        print(f"O Veiculo esta se movendo") 
    

class Carro(Veiculo):
    def __init__(self, marca:str = None, modelo:str = None, __placa:str = None):
        super().__init__( marca, modelo)
        self.__placa = __placa

    def __str__(self):
        return f"Carro da placa: {self.__placa} cadastrado com sucesso"
    
    def mover(self) -> None:
        super().mover()
        print(f"O carro está dirigindo")
    
    def trocar_placa(self, placa_nova:str) -> str:
        if placa_nova != self.__placa:
            self.__placa = placa_nova
            print(f"A placa do carro foi alterada para: {self.__placa}")
        else:
            print(f"A placa fornecida é igual a antiga ou nao é um campo de texto")

    

class Bicicleta(Veiculo):
    def __init__(self, marca:str = None, modelo:str = None, _marchas:int = 0, marcha_atual:int = 0, velocidade_atual:float = 0.0):
        super().__init__( marca, modelo)
        self._marchas = _marchas
        self.marcha_atual = marcha_atual
        self.velocidade_atual = velocidade_atual

    def __str__(self):
        return f"Bicicleta de {self._marchas} foi cadastrada com sucesso"
    
    def mover(self) -> None:
        super().mover()
        self.velocidade_atual += 1.5
        print(f"A bicicleta está pedalando")
    
    def trocar_numero_marchas(self, nova_marcha:int) -> str:
        if nova_marcha != self._marchas and nova_marcha >= 1:
            self._marchas = nova_marcha
            print( f"A bicicleta agora tem: {self._marchas} marchas")
        else:
            print(f"A bicicleta ja tem esse numero de marchas ou voce digitou um campo nao inteiro")

        
    
    def acelerar(self, velocidade:float) -> str:
        if velocidade < self.velocidade_atual and velocidade > 0.0:
            if self.marcha_atual > 0:
                self.marcha_atual -= 1
                self.velocidade_atual = velocidade
                print(f"A bicicleta diminuiu uma marcha e agora esta com a veolocidade de: {self.velocidade_atual} km e na {self.marcha_atual} marcha")
            else:
                print("A bicicleta ja esta na sua primeira marcha e nao pode reduzir mais")
        elif velocidade > self.velocidade_atual and self.marcha_atual < self._marchas:
            self.marcha_atual += 1
            self.velocidade_atual = velocidade
            if self.marcha_atual == self._marchas:
                print(f"Voce chegou na ultima marcha, agora tem que desacelerar")
            print(f"A bicicleta aumentou uma marcha e agora esta com a veolocidade de: {self.velocidade_atual} km e na {self.marcha_atual} marcha")
        elif self.marcha_atual == self._marchas:
            print(f"Voce chegou na ultima marcha, agora tem que desacelerar")
        else:
            print(f"A bicicleta já está parada, voce nao pode diminuir a marcha ou forneceu a velocidade de maneira errada")

print("\n")

vei1 = Veiculo("ford", "fg211")
print(vei1)
vei1.mover()

print("\n")

vei2 = Carro("wolksvagen", "tcross", "10XA21")
print(vei2)
vei2.mover()
vei2.trocar_placa("34JIA5")

print("\n")

vei3 = Bicicleta("monark", "cic002", 5)
print(vei3)
vei3.mover()
vei3.trocar_numero_marchas(8)
vei3.acelerar(2.5)
vei3.acelerar(1.5)
vei3.acelerar(0.2)
vei3.trocar_numero_marchas(3)
vei3.acelerar(1.5)
vei3.acelerar(2.5)
vei3.acelerar(3.5)
vei3.acelerar(4.5)
vei3.acelerar(5.5)




