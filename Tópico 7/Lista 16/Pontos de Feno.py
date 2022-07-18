# Pega o número de palavras do dicionário hay points e descrições
palavras, descricoes = [int(x) for x in input().split()]

# Cria o dicionário de hay points
hay_points = {}

# Pra cada palavra
for _ in range(palavras):
    # Pega a palavra e o valor
    entrada = input().split()

    # Adiciona a palavra como chave e o valor como valor no dicionario de hay points
    hay_points[entrada[0]] = int(entrada[1])

# Pra cada descrição
for _ in range(descricoes):
    # Lista de cada palavra da descrição
    descricao_texto = input().split()

    descricao_valor = sum(
        hay_points[palavra]
        for palavra in descricao_texto
        if palavra in hay_points
    )


    # Printa o valor da descrição
    print(descricao_valor)

   