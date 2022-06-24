#Funções Básicas de entrada e saída
#Exemplo 1
#Imprimir (mostrar) um texto
print ("Ola Mundo!")
#ficar atento ao tipo:
print ("2+3")          # imprime    2+3   
print ("2" + "3")      # imprime    23
print (2+3)            # imprime    5

# Exemplo 2
# É possível imprimir vários valores, separando-os com vírgulas
data = "23/05/2020"
local = "Florianópolis"
print("Hoje é", data, "e estamos em", local, ".")  #imprime: Hoje é 23/05/2020 e estamos em Florianópolis.

# Exemplo 3
# A função print adiciona automaticamente uma quebra de linha ao final
print()
print("Uma linha")
print("Outra linha")

# Exemplo 4
# Para evitar a quebra de linha, utilize o parâmetro "end="
print("Hoje", end="")
print("Amanhã", end=" ****** ")
print("Depois de amanhã",end="")
print("fim")