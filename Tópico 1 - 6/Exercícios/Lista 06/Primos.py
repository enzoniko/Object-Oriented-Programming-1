def quantidade_primos_intervalo(num1, num2):
    primos = 0
    for numero in range(num1, num2 + 1):
        divisores = 0
        for divisor in range(2, numero):
            if numero % divisor == 0:
                divisores += 1
        if divisores == 0:
            primos += 1
            
    return primos

num1, num2 = [int(num) for num in input("Digite o início e o fim do intervalo separados por um espaço: ").split()]

print(quantidade_primos_intervalo(num1, num2))
