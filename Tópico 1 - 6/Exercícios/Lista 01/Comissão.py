# Pega o nome do usuário
nome = input("Qual seu nome? ")

# Pega o salário fixo do usuário
salario_fixo = float(input("Qual seu salário fixo? "))

# Pega o valor total das vendas desse usuário
total_vendas = float(input("Qual foi o valor total de suas vendas? "))

# Printa o salário final do usuário, somando o salário fixo mais a comissão de 15% pelo valor total de vendas
print("TOTAL = {:.2f}".format(salario_fixo + (0.15 * total_vendas)))
