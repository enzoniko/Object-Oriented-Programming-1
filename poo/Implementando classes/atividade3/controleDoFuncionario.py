from funcionario import Funcionario

def calcular_aumento_funcionario(nome, salario):
    return Funcionario(nome, salario).getInfo()

for i in range(3):
    nome, salario = input("Digite o nome e o salário do funcionário: ").split()[:2]
    print(calcular_aumento_funcionario(nome, float(salario)))