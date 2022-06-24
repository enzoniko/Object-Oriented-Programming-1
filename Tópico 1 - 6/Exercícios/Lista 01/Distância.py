# Pega x e y do ponto 1
p1x, p1y = input("Digite x e y do ponto 1 separados por um espaço: ").split()

# Pega x e y do ponto 2
p2x, p2y = input("Digite x e y do ponto 2 separados por um espaço: ").split()

# Calcula a distância entre os pontos convertidos em float
distancia = (((float(p1x) - float(p2x))**2) + ((float(p1y) - float(p2y))**2)) ** 0.5

# Printa a distância
print("{:.4f}".format(distancia))
