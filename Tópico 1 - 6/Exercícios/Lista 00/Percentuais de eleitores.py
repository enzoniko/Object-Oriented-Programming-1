# 1) Escreva um algoritmo para ler o número total de eleitores de um município, o número de votosbrancos, nulos e válidos.
# 2) Seu programa deve verificar se a soma de brancos, nulos e válidos equivalem a 100% do número de eleitores que votaram.
# 3) Calcular e escrever o percentual que cada um representa em relação ao total de eleitores.

# 1)
# Pergunta ao usuário o número total de eleitores do município
total_eleitores = int(input("Qual o número total de eleitores do município? "))

# Pergunta ao usuário o número de votos em branco
votos_brancos = int(input("Qual o número de votos em branco? "))

# Pergunta ao usuário o número de votos nulos
votos_nulos = int(input("Qual o número de votos nulos? "))

# Pergunta ao usuário o número de votos válidos
votos_validos = int(input("Qual o número de votos válidos? "))

# 2)
# Calcula a porcentagem que a soma dos votos representa com relação ao total de eleitores 
porcentagem_votos = ((votos_brancos + votos_nulos + votos_validos) / total_eleitores) * 100

# 3)
# Calcula as porcentagens dos votos com relação ao total de eleitores
porcentagem_votos_brancos = (votos_brancos / total_eleitores) * 100
porcentagem_votos_nulos = (votos_nulos / total_eleitores) * 100
porcentagem_votos_validos = (votos_validos / total_eleitores) * 100

# Printa para o usuário todos os percentuais calculados
print("")
print(f"Percentual de votos em branco: {porcentagem_votos_brancos}%")
print(f"Percentual de votos nulos: {porcentagem_votos_nulos}%")
print(f"Percentual de votos válidos: {porcentagem_votos_validos}%")
print(f"Percentual de votos com relação ao número total de eleitores do município: {porcentagem_votos}%")





