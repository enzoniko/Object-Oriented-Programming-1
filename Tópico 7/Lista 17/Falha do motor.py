medidas = int(input())
rotacoes = [int(x) for x in input().split()][:medidas]
quedas = []
for i in range(1, len(rotacoes)):
    if rotacoes[i] < rotacoes[i-1]:
        quedas.append(i)
        break
if not quedas:
    print(0)
else:
    print(quedas[0] + 1)
