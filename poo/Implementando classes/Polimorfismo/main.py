from carro import Carro
from veiculo import Veiculo

# Inicio tests
c1 = Carro("Azul", "Ford", "Fusion", 10, 2019)
c2 = Carro("Vermelho", "Chevrolet", "Onix", 10, 2019)
c3 = Carro("Preto", "Fiat", "Uno", 10, 2019)
v = Veiculo("Azul", "Tesla", "X10", 60)

c1.imprime()
c2.imprime()
c3.imprime()
v.imprime()

c1.abastecer(10)
c2.abastecer(20)
c3.abastecer(50)
v.abastecer(50)

c1.imprime()
c2.imprime()
c3.imprime()
v.imprime()

v.set_limit(130)
v.abastecer(70)
v.imprime()
# Fim tests
