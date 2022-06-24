operacao = input()
n = 12
matriz = [0] * n

for i in range(len(matriz)):
    matriz[i] = [0] * n

for l in range(len(matriz)):
    for c in range(n):
        matriz[l][c] = float(input())

soma = 0
count = 0

for l in range(len(matriz)):
    for c in range(l):
        soma += matriz[l][c]
        count += 1
        
if operacao.upper() == 'S':
    print('{:.1f}'.format(soma))
    
elif operacao.upper() == 'M':
    print('{:.1f}'.format(soma/count))

