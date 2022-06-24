quantidade_par = 0
quantidade_impar = 0
for x in range(10):
    inteiro = int(input("Número: "))
    if inteiro % 2 == 0:
        quantidade_par += 1
    else:
        quantidade_impar += 1

print ("Quantidade de números pares: ", quantidade_par)
print ("Quantidade de números ímpares: ", quantidade_impar)
