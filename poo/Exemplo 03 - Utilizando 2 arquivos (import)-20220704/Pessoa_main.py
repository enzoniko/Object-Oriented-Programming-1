#Exemplo 03

#main

from Pessoa import Pessoa

pessoa1 = Pessoa("Ana", 25,True)
pessoa2 = Pessoa("Paulo",50)

print(f"Dados da pessoa1: {pessoa1.getNome()} - {pessoa1.getIdade()} anos.", )
print("Status: ", pessoa1.comendo)

print(f"Dados da pessoa2: {pessoa2.getNome()} - {pessoa2.getIdade()} anos.", )
print("Status: ", pessoa2.comendo)
