def numeros_necessarios_para_ultrapassar_z(x, z):
    acumulador = 0
    numeros_necessarios = 0
    while z <= x:
        z = int(input("Z: "))

    while acumulador <= z:
        acumulador += x
        x += 1
        numeros_necessarios += 1

    print(numeros_necessarios)

numeros_necessarios_para_ultrapassar_z(int(input("X: ")), int(input("Z: ")))