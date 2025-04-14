# Intalando pacotes:
# python -m pip install --upgrade pip --user
# pip install pyqt5

class Veiculo:
    def __init__(self, modelo =None, ano = 2025):
        self.modelo = modelo
        self.ano = ano

    def __str__(self):
        return f"Modelo: {self.modelo}\nAno: {self.ano}"