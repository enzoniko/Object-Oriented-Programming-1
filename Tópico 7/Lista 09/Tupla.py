tupla = (3, 2, 10, 4, 5, 6, 7, 8, 9, 1)

def maior_valor(valores):
    valor_maior = 0
    for i in range(len(valores)):
        if valores[i] >= valor_maior:
            valor_maior = valores[i]
    return valor_maior

def menor_valor(valores):
    valor_menor = 10
    for i in range(len(valores)):
        if valores[i] <= valor_menor:
            valor_menor = valores[i]
    return valor_menor

print(f"Posição do maior valor: {tupla.index(maior_valor(tupla))}")
print(f"Posição do menor valor: {tupla.index(menor_valor(tupla))}")

