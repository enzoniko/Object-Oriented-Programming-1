# Pergunta o valor da casa
valor_casa = float(input("Qual o valor da casa? "))

# Pergunta o salário do comprador
salario = float(input("Qual o seu salário? "))

# Pergunta em quantos anos ele vai pagar o empréstimo bancário
anos = int(input("Em quantos anos você pretende pagar a casa? "))

# Divide o valor da casa pelo quantidade de anos que ele vai pagar o empréstimo para calcular as prestações
valor_mensal = valor_casa / anos 

# Se o valor da prestação for menor ou igual do que 30% do salário do comprador aprova o empréstimo
if (valor_mensal <= 0.3 * salario):
    print("Empréstimo aprovado!")

# Se o valor da prestação for maior do que 30% do salário do comprador nega o empréstimo
else:
    print("Empréstimo negado :(")