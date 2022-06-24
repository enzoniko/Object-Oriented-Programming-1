tempo = int(input("Tempo da viagem: "))
velocidade_media = int(input("Velocidade média da viagem: "))
litros = (velocidade_media * tempo) / 12
print("{:.3f}".format(litros))