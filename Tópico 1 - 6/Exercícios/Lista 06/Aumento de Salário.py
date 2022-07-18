def aumento_de_salario(salario):
    
    if salario > 0 and salario <= 400:
        percentual = 15
    elif salario > 400 and salario <= 800:
        percentual = 12
    elif salario > 800 and salario <= 1200:
        percentual = 10
    elif salario > 1200 and salario <= 2000:
        percentual = 7
    else:
        percentual = 4

    reajuste = salario * (percentual / 100)
    novo_salario = salario + reajuste
    print(f'Novo Salário: {novo_salario}')
    print(f'Reajuste Ganho: {reajuste}')
    print(f'Em percentual: {percentual}%')
        
aumento_de_salario(float(input('Salário: ')))