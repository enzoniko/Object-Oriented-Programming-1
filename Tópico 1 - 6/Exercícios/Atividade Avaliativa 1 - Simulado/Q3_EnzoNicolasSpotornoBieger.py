# Enzo Nicolás Spotorno Bieger - 22100614

def controle_capacidade():
    leituras, capacidade = [int(valor) for valor in input('Digite a quantidade de leituras e capacidade máxima do elevador separados por um espaço: ').split()]
    capacidade_excedida = False
    pessoas_dentro = 0
    for iterador in range(leituras):
        saidas, entradas = [int(num) for num in input("Digite quantas pessoas saíram e quantas entraram nesse andar separados por um espaço: ").split()]
        pessoas_dentro += entradas - saidas 
        if pessoas_dentro > capacidade:
            capacidade_excedida = True

    if capacidade_excedida == True:
        print("S")
    else:
        print("N")

controle_capacidade()