aux = 0
count = 1
while True:
    valor = int(input("Valor: "))
    aux = valor
    if aux == 0:
        break
    print(f"Teste {count}")
    count += 1
   
    notas_50 = 0
    notas_10 = 0
    notas_5 = 0
    notas_1 = 0

    while valor != 0:
        while (valor - 50) >= 0:
            valor -= 50
            notas_50 += 1
        while (valor - 10) >= 0:
            valor -= 10
            notas_10 += 1
        while (valor - 5) >= 0:
            valor -= 5
            notas_5 += 1
        while (valor - 1) >= 0:
            valor -= 1
            notas_1 += 1
    print(f"{notas_50} {notas_10} {notas_5} {notas_1}")

