linha = int(input())
operacao = input()
n = 12
matriz = [0] * n
for i in range(len(matriz)):
    matriz[i] = [0] * n

for l in range(len(matriz)):
    for c in range(n):
        matriz[l][c] = float(input())

for l in matriz:
    if matriz.index(l) == linha:
        soma = sum(l)
        if operacao.upper() == 'S':
            print('{:.1f}'.format(soma))
        elif operacao.upper() == 'M':
            print('{:.1f}'.format(soma/len(l)))
 