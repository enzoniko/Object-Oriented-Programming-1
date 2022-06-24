def num_perfeito(num):
    divisores = set()
    for x in range(1, num):
        if num%x == 0:
            divisores.add(x)
    soma_divisores = 0
    for n in divisores:
        soma_divisores += n
    if soma_divisores == num:
        return str(num) + ' eh perfeito'
    else:
        return str(num) + ' não eh perfeito'


casos = int(input())
for i in range(casos):
    print(num_perfeito(int(input())))