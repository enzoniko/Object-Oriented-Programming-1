soma = 0
count = 0
while True:
    n = int(input("Digite um número: "))
    soma += n
    count += 1
    parar = input("Você quer parar (s/n)? ")
    if parar == "s":
        break
print (f"A média dos números digitados é: {soma / count}")