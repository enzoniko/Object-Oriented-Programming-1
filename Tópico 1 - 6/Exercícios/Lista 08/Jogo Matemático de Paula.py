def jogo_paula(sequencia):

    digito_1 = int(sequencia[0])
    letra = sequencia[1]
    digito_2 = int(sequencia[2])

    if digito_1 == digito_2:
        return digito_1*digito_2
    elif letra.upper() == letra:
        return digito_2 - digito_1
    else:
        return digito_1 + digito_2

n = int(input())
for _ in range(n):
    sequencia = input()
    value = jogo_paula(sequencia)
    print(value)