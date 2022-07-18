def num_perfeito(num):
    divisores = {x for x in range(1, num) if num%x == 0}
    soma_divisores = sum(divisores)
    if soma_divisores == num:
        return f'{str(num)} eh perfeito'
    else:
        return f'{str(num)} não eh perfeito'


casos = int(input())
for _ in range(casos):
    print(num_perfeito(int(input())))