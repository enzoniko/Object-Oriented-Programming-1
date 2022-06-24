n = int(input("Digite a quantidade de valores da lista: "))
x = []
for i in range(n):
    x.append(int(input("Digite um elemento da lista: ")))

k = int(input("Digite um valor para multiplicar por todos os elementos da lista: "))

for i in range(len(x)):
    x[i] *= k

print(f"Lista resultante: {x}")
