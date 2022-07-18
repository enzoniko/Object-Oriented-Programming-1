n = int(input())
lista_num_minas = []

campo = [int(input()) for _ in range(n)]
print()

for i in range(n):
    if i == 0:
        num_minas = campo[i] + campo[i+1]
    elif i == len(campo) - 1:
        num_minas = campo[i] + campo[i-1]
    else:
        num_minas = campo[i-1] + campo[i] + campo[i+1]
    lista_num_minas.append(num_minas)

    print(lista_num_minas[i])

    

