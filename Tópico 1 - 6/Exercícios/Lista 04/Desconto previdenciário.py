parar = ''
while parar != 's':
    salario = float(input("Qual seu salário? "))
    desconto = salario * 0.11
    if desconto < 320:
        print(f"O desconto é de {desconto} reais")
    else:
        print("O desconto é de 320 reais que corresponde à {:.2f}% de desconto".format((320 * 100 / salario)))
    parar = input("Quer parar (s/n)? ")
    