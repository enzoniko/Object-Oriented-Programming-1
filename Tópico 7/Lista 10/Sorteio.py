n = int(input())
for i in range(n):
    qt, s = [int(x) for x in input().split()]
    chutes = [int(x) for x in input().split()]
    if s in chutes:
        print(chutes.index(s) + 1)
    else:
        menor_diff = 1000
        chute_mais_prox = 0
        for c in range(len(chutes)):
            if chutes[c] > s and (chutes[c] - s) < menor_diff:
                menor_diff = chutes[c] - s
                chute_mais_prox = chutes[c]
            elif chutes[c] < s and (s - chutes[c]) < menor_diff:
                menor_diff = s - chutes[c]
                chute_mais_prox = chutes[c]
        print(chutes.index(chute_mais_prox) + 1)
                