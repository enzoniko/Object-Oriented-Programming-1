# Pergunta ao usuário quantos anos, meses e dias de idade ele tem convertendo os valores para inteiros
anos, meses, dias = [int(value) for value in input("Digite quantos anos, meses e dias de idade você têm, separados por um espaço em branco: ").split()]

# converte os anos e meses em dias e soma os dias restantes para obter a idade do usuário em dias
idade_em_dias = anos*365 + meses*30 + dias

# Printa pro usuário a idade dele em dias
print(f"Sua idade em dias é: {idade_em_dias}")
