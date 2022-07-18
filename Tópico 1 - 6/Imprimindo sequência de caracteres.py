#Imprimindo Sequencia de Caracteres

# Formatação utilizando o método "format"
# Cada ocorrência de '{}' será substituída pelo correspondente valor passado no comando "format"
hoje = f'Hoje é dia {16} de {"junho"} de {2021}'
print(hoje)

# É também possível nomear os argumentos (um nome entre {}) 
# e definir o valor destes nomes no comando format.
print("Hoje é dia {dia} de {mes} de {ano}".format(dia=1, mes='setembro', ano=2020))

# No caso de valores reais, podemos definir o número de dígitos a serem apresentadas após o ponto decimal
print(f"O valor de PI é {3.14159265}")
print("O valor de PI é {:.3f}".format(3.14159265))

# Dentro de {} também é possível definir o tamanho (número de caracteres) total do campo
print("O saltador {:10} saltou {:7}".format('Luiz', 7.23)) #Dúvida aqui, porque no segundo campo os caracteres vazios foram adicionados antes?
print("O saltador {:10} saltou {:7}".format('Marcos', 7.05))
print("O saltador {nome:10} saltou {distancia:7}".format(nome='Pedro', distancia=7.8))
print("O saltador {nome:10} saltou {distancia:7}".format(nome='João', distancia=6.98))

# Outra alternativa para formatação de strings
# é iniciá-los com a letra f ou F vez de utilizar o método .format()
import math
dia = 31
mes = 'dezembro'
ano = 2020
data = f'Hoje é dia {dia} de {mes} de {ano}'
print(data)

print(f'O valor de PI é aproximadamente {math.pi:.3f}.')