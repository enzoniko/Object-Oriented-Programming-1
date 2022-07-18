#Entrada de dados via teclado

# A função input() permite obter os dados que forem digitados via teclado
texto = input("Digite algo: ")
print(f"Texto digitado: {texto}")

# É possível incluir um texto explicativo que é apresentado ao usuário no momento da digitação
nome = input("Digite seu nome: ")
print(nome)

# Obtendo um número inteiro: a string digitada é convertida para o número inteiro por meio da função int()
idade = int(input("Digite sua idade: "))
print(idade)

# Obtendo um número real: a string digitada é convertida para o número real por meio da função float()
pi = float(input("Valor de PI: "))
print(pi)

# Obter o nome e a idade de uma pessoa via teclado, e imprimir
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
print(f"O nome é {nome} e a idade é {idade}")

# No caso de serem digitados vários valores numa mesma linha,
#pode-se separá-los em variáveis utilizando o método "split".
x, y, z = input("Digite três valores inteiros, um ao lado do outro, separados por um espaço em branco: ").split()

# convertendo as strings digitados para números inteiros
x = int(x)
y = int(y)
z = int(z)
print(x, y, z)

# Alternativamente, pode ser também escrito conforme abaixo.
x, y, z = [int(value) for value in input("Digite trẽs valores inteiro, um ao lado do outro: ").split()]
print(x, y, z)