# Enzo Nicolás Spotorno Bieger - 22100614

def funcao():
    soma_idades = 0
    quantidade_idades = 0
    quantidade_mulheres_salario_maior_2000 = 0
    maior_idade = 0
    nome_mais_velho = 0
    menor_salario = 1000000
    while True:
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        sexo = input("Sexo: [M/F]")
        salario =  float(input("Salário: "))

        soma_idades += idade
        quantidade_idades += 1

        if salario < menor_salario:
            menor_salario = salario
            sexo_menor_salario = sexo
            idade_menor_salario = idade


        if idade > maior_idade:
            maior_idade = idade
            nome_mais_velho = nome

        if sexo == 'F' and salario > 2000:
            quantidade_mulheres_salario_maior_2000 += 1

        continuar = input("Deseja continuar cadastrando? [S/N]")
        if continuar.upper() == 'N':
            break
    media_idades = soma_idades / quantidade_idades
    print()
    print(f'Média das Idades: {media_idades}')
    print(f'Quantidade de mulheres com salário maior do que 2000: {quantidade_mulheres_salario_maior_2000}')
    print(f'Sexo da pessoa com menor salário: {sexo_menor_salario}')
    print(f'Idade da pessoa com menor salário: {idade_menor_salario}')
    print(f'Nome do morador mais velho: {nome_mais_velho}')

funcao()
print("Programa Finalizado")
        
    

    