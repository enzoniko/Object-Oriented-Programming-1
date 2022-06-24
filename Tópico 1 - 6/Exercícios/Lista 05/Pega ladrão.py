
while True:
    distancia = int(input("Qual a distância entre a guarda costeira e o fugitivo? "))
    velocidade_fugitivo = int(input("Qual a velocidade do fugitivo? "))
    velocidade_guarda = int(input("Qual a velocidade da guarda costeira? "))
    tempo_fugitivo = 12 / velocidade_fugitivo
    tempo_guarda = ((distancia ** 2) + 144)**0.5 / velocidade_guarda
    if tempo_fugitivo >= tempo_guarda:
        print("S")
    else:
        print("N")