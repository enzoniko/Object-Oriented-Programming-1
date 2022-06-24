valor = float(input("Valor: "))

notas_100 = 0
notas_50 = 0
notas_20 = 0
notas_10 = 0
notas_5 = 0
notas_2 = 0
moedas_1 = 0
moedas_05 = 0
moedas_025 = 0
moedas_01 = 0
moedas_005 = 0
moedas_001 = 0

while valor != 0:
    while (valor - 100) >= 0:
        valor -= 100
        notas_100 += 1
    while (valor - 50) >= 0:
        valor -= 50
        notas_50 += 1
    while (valor - 20) >= 0:
        valor -= 20
        notas_20 += 1
    while (valor - 10) >= 0:
        valor -= 10
        notas_10 += 1
    while (valor - 5) >= 0:
        valor -= 5
        notas_5 += 1
    while (valor - 2) >= 0:
        valor -= 2
        notas_2 += 1
    while (valor - 1) >= 0:
        valor -= 1
        moedas_1 += 1
    while (valor - 0.5) >= 0:
        valor -= 0.5
        moedas_05 += 1
    while (valor - 0.25) >= 0:
        valor -= 0.25
        moedas_025 += 1
    while (valor - 0.10) >= 0:
        valor -= 0.10
        moedas_01 += 1
    while (valor - 0.05) >= 0:
        valor -= 0.05
        moeda_005 += 1
    while (valor - 0.01) >= 0:
        valor -= 0.01
        moedas_001 += 1
    break

'''
valor = valor * 100
notas_100 = valor // 10000
valor = valor % 10000
notas_50 = valor // 5000
valor = valor % 5000
notas_20 = valor // 2000
valor = valor % 2000
notas_10 = valor // 1000
valor = valor % 1000
notas_5 = valor // 500
valor = valor % 500
notas_2 = valor // 200
valor = valor % 200
moedas_1 = valor // 100
valor = valor % 100
moedas_05 = valor // 50
valor = valor % 50
moedas_025 = valor // 25
valor = valor % 25
moedas_01 = valor // 10
valor = valor % 10
moedas_005 = valor // 5
valor = valor % 5
moedas_001 = valor // 1
valor = valor % 1
'''

print("NOTAS:")
print("Notas de 100: {}".format(int(notas_100)))
print("Notas de 50: {}".format(int(notas_50)))
print("Notas de 20: {}".format(int(notas_20)))
print("Notas de 10: {}".format(int(notas_10)))
print("Notas de 5: {}".format(int(notas_5)))
print("Notas de 2: {}".format(int(notas_2)))
print("MOEDAS:")
print("Moedas de 1: {}".format(int(moedas_1)))
print("Moedas de 0.5: {}".format(int(moedas_05)))
print("Moedas de 0.25: {}".format(int(moedas_025)))
print("Moedas de 0.10: {}".format(int(moedas_01)))
print("Moedas de 0.05: {}".format(int(moedas_005)))
print("Moedas de 0.01: {}".format(int(moedas_001)))

