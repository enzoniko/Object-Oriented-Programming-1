inteiro1 = int(input("Número 1: "))
inteiro2 = int(input("Número 2: "))
soma = 0
for x in range(inteiro1, inteiro2 + 1):
    print(x)
    soma += x
    
print("Soma: ", soma)