
def media_idades():
    soma_idades = 0
    quantidade_idades = 0
    while True:
        idade = int(input("Qual a idade? "))
        if idade < 0:
            break
        
        soma_idades += idade
        quantidade_idades += 1

    print(soma_idades/quantidade_idades)
    

media_idades()