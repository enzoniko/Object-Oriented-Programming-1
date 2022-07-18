num_praias = int(input("Quantas praias você deseja cadastrar? "))
soma_distancias = 0
praia_mais_distante = ''
maior_distancia = 0
contagem_praias_entre_15_e_20_kilometros = 0
for _ in range(num_praias):
    nome_praia = input("Qual o nome da praia? ")
    distancia_praia = int(input("Qual a distância da praia até o centro? "))

    if distancia_praia > maior_distancia:
        maior_distancia = distancia_praia
        praia_mais_distante = nome_praia

    if distancia_praia >= 15 and distancia_praia <= 20:
        contagem_praias_entre_15_e_20_kilometros += 1

    soma_distancias += distancia_praia
print(f"A praia mais distante do centro da cidade é {praia_mais_distante}!")
print(f"Número de praias entre 15 e 20 kilometros de distância do centro: {contagem_praias_entre_15_e_20_kilometros}")
print("A distância média das praias ao centro da cidade é: {:.1f} kilometros".format(soma_distancias / num_praias)) 
    