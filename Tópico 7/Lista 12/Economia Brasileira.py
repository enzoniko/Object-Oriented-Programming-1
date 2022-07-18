pessoas = int(input())
opinioes = [int(x) for x in input().split()][:pessoas]
soma = sum(opinioes)
if soma / pessoas < 0.5:
    print('Y')
else:
    print('N')
