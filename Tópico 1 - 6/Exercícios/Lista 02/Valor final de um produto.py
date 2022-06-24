# Lê o valor do produto
valor = float(input("Qual o valor do produto? "))

# Lê a condição de pagamento
jeito_de_pagar = input("Escolha a condição de pagamento (1: à vista; 2: 1x no cartão; 3: 2x no cartão; 4: 3x no cartão): ")

# Se a condição de pagamento for à vista
if jeito_de_pagar == "1":
    valor -= 0.1*valor
    print(f"O valor final é: {valor}")
elif jeito_de_pagar == "2":
    valor -= 0.05*valor
    print(f"O valor final é: {valor}")
elif jeito_de_pagar == "3":
    print(f"O valor final é: {valor}")
elif jeito_de_pagar == "4":
    valor -= 0.2*valor
    print(f"O valor final é: {valor}")
else:
    print("Condição de pagamento inválida")
    