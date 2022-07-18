x = []

for _ in range(10):
    valor = int(input())
    if valor <= 0:
        x.append(1)
    else:
        x.append(valor)

for i in range(len(x)):
    print(f"x[{i}] = {x[i]}")
    