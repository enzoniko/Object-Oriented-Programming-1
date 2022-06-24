n = int(input("Número de elementos: "))
lista = []
for i in range(n):
    num = int(input("Digite um número: "))
    lista.append(num)

cont = 0
for i in range(len(lista)):
    if lista.count(lista[i]) > 1:
        cont += 1
        break
if cont >= 1:
    print("Tem número repetido")
else:
    print("Não tem número repetido")
    