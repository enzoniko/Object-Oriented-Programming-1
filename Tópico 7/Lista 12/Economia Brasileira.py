pessoas = int(input())
opinioes = [int(x) for x in input().split()][0:pessoas]
soma = 0
for o in opinioes:
    soma += o
if soma / pessoas < 0.5:
    print('Y')
else:
    print('N')
