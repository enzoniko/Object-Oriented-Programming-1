contador_positivos = 0
soma_positivos = 0
for _ in range(6):
    numero = float(input("Digite um número: "))
    if numero > 0:
        contador_positivos += 1
        soma_positivos += numero
print(f'{contador_positivos} valores positivos')
print(soma_positivos/contador_positivos)
    
    