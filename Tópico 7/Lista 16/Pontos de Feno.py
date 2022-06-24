# Pega o número de palavras do dicionário hay points e descrições
palavras, descricoes = [int(x) for x in input().split()]

# Cria o dicionário de hay points
hay_points = dict()

# Pra cada palavra
for palavra in range(palavras):

    # Pega a palavra e o valor
    entrada = input().split()
    
    # Adiciona a palavra como chave e o valor como valor no dicionario de hay points
    hay_points[entrada[0]] = int(entrada[1])

# Pra cada descrição
for descricao in range(descricoes):

    # Lista de cada palavra da descrição
    descricao_texto = input().split()

    descricao_valor = 0

    # Pra cada palavra da descrição
    for palavra in descricao_texto:

        # Se a palavra existe no dicionario de hay points
        if palavra in hay_points:

            # Adiciona o valor da palavra ao valor da descrição
            descricao_valor += hay_points[palavra]
    
    # Printa o valor da descrição
    print(descricao_valor)

   