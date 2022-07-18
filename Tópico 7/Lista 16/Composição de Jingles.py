# Dicionário de durações dos compassos
duracao_compassos = {'W': 1, 'H': 1/2, 'Q': 1/4, 'E': 1/8, 'S': 1/16, 'T': 1/32, 'X': 1/64}

# Calcula a quantidade de compassos corretos
def quantidade_compassos_corretos(compassos):

    compassos_corretos = 0

    # Pra cada compasso na composição
    for compasso in compassos:

        duracao = 0

        # Se o compasso não for vazio
        if len(compasso) > 0:

            # Pra cada nota no compasso
            for nota in compasso:

                # Soma a duração da nota
                duracao += duracao_compassos[nota]

        # Se a duração for correta (1)
        if duracao == 1:

            # Incrementa a quantidade de compassos corretos
            compassos_corretos += 1

    # Retorna a quantidade de compassos corretos
    return compassos_corretos 

# Enquanto o usuário não digitar * roda o programa
while True:

    # Pega a composição
    compassos = input().split('/')

    if compassos == ['*']:
        break

    # Printa a quantidade de compassos corretos
    print(quantidade_compassos_corretos(compassos))