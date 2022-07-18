n = int(input())

total_cobaias = 0
coelhos = 0
ratos = 0
sapos = 0

for _ in range(n):
    cobaias, tipo = list(input().split())
    cobaias = int(cobaias)
    total_cobaias += cobaias

    if tipo == 'C':
        coelhos += cobaias
    elif tipo == 'R':
        ratos += cobaias
    else:
        sapos += cobaias

percentual_coelhos = (coelhos/total_cobaias) * 100
percentual_ratos = (ratos/total_cobaias) * 100
percentual_sapos = (sapos/total_cobaias) * 100

print(f"Total: {total_cobaias} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print("Percentual de coelhos: {:.2f}%".format(percentual_coelhos))
print("Percentual de ratos: {:.2f}%".format(percentual_ratos))
print("Percentual de sapos: {:.2f}%".format(percentual_sapos))


