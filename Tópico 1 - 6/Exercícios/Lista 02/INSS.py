# Atribui à variável "salario" um valor digitado pelo usuário
salario = float(input("Digite seu salário bruto: "))

# Se o salário for menor ou igual à 720
if (salario <= 720):
    
    # Aplica juros de 7,65% no salário e atribui o resultado à variável "inss"
    inss = salario * 0.0765

# Se o salário for menor ou igual à 1200
elif (salario <= 1200):
    
    # Aplica juros de 9% no salário e atribui o resultado à variável "inss"
    inss = salario * 0.09
    
# Se o salário for menor ou igual à 2400
elif (salario <= 2400):
    
    # Aplica juros de 11% no salário e atribui o resultado à variável "inss"
    inss = salario * 0.11
    
# Se o salário for maior do que 2400
else:
    
    # Aplica juros de 11% sobre 2400 e atribui o resultado à variável "inss"
    inss = 2400 * 0.11
    
print(f"INSS: {inss}")