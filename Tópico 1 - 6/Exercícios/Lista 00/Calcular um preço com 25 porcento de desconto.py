# Pergunta ao usuário o preço de determinado produto e o converte para float
price = float(input("Qual o preço do produto? "))

# Calcula o preço do produto com desconto de 25%
discounted_price = price - ((25/100) * price)

# Printa pro usuário o preço do produto com desconto
print(f"O preço com 25% de desconto é: {discounted_price}")