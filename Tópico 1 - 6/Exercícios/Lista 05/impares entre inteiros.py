n = int(input("Quantos casos? "))

for x in range(n + 1):
    soma = 0
    x, y = [int(i) for i in input("Digite 2 valores separados por um espaço: ").split()]
    if x < y:
        for m in range(x + 1, y):
            if m % 2 != 0:
                soma += m
    elif x > y:
        for m in range(y + 1, x):
            if m % 2 != 0:
                soma += m

    print(soma)
    