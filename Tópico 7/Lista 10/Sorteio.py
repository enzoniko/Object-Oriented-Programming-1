n = int(input())
for _ in range(n):
    qt, s = [int(x) for x in input().split()]
    chutes = [int(x) for x in input().split()]
    if s in chutes:
        print(chutes.index(s) + 1)
    else:
        menor_diff = 1000
        chute_mais_prox = 0
        for chute in chutes:
            if chute > s and chute - s < menor_diff:
                menor_diff = chute - s
                chute_mais_prox = chute
            elif chute < s and s - chute < menor_diff:
                menor_diff = s - chute
                chute_mais_prox = chute
        print(chutes.index(chute_mais_prox) + 1)
                