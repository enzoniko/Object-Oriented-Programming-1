# Pega o tempo gasto na viagem
tempo = int(input("Tempo gasto na viagem (horas): "))

# Pega a velocidade média durante a viagem
velocidade_media = int(input("Velocidade média durante a viagem (Km/H): "))

# Calcula a distância da viagem
distancia = tempo * velocidade_media

# Calcula os litros gastos na viagem
litros = distancia / 12

# Printa a quantidade de litros gastos na viagem
print("{:.3f}".format(litros))