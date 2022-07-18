pedras, sapos = [int(x) for x in input().split()]
pedras = [0] * pedras
pedras_possiveis = set()
for _ in range(sapos):
    posicao_inicial, distancia = [int(x) for x in input().split()]
    i = 0
    while (posicao_inicial - 1) - (distancia * i) >= 0:
        pedras_possiveis.add(posicao_inicial - (distancia * i))
        i += 1
    i = 0
    while (posicao_inicial - 1) + (distancia * i) <= len(pedras) - 1:
        pedras_possiveis.add(posicao_inicial + (distancia * i))
        i += 1

for i in pedras_possiveis:
    pedras[i - 1] = 1

for i in range(len(pedras)):
    print(pedras[i])
        