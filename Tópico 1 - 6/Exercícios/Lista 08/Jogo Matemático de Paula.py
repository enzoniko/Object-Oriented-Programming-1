def jogo_paula(sequencia):
    
    digito_1 = int(sequencia[0])
    letra = sequencia[1]
    digito_2 = int(sequencia[2])

    if digito_1 == digito_2:
        valor = digito_1*digito_2
    elif letra.upper() == letra:
        valor = digito_2 - digito_1
    else:
        valor = digito_1 + digito_2
        
    return valor

n = int(input())
for i in range(n):
    sequencia = input()
    value = jogo_paula(sequencia)
    print(value)