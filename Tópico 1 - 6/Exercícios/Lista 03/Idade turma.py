n = int(input("Número de pessoas: "))
soma_idades = 0
for _ in range(n):
    idade = int(input("Sua idade: "))
    soma_idades += idade
if 0 < (soma_idades / n) <= 25:
    print("A turma é jovem")
elif 25 < (soma_idades / n) <= 60:
    print("A turma é adulta")
else:
    print("A turma é idosa")
    
