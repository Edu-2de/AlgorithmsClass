from Fila import Fila
from Carro import Carro

fila = Fila()
fila.imprimir()

c1 = Carro("Pulse", 2025, "ABC-1234")
fila.add(c1)
c2 = Carro("Renegade", 2021, "RMY-8C04")
fila.add(c2)
c3 = Carro("Doblo", 2005, "HDK-4391")
fila.add(c3)

fila.lavar()
fila.lavar()
fila.lavar()
