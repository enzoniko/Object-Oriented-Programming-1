dias, saldo = [int(x) for x in input().split()]
menor_saldo = saldo
for _ in range(dias):
    movimentacao = int(input())
    saldo += movimentacao
    if saldo < menor_saldo:
        menor_saldo = saldo
print(menor_saldo)