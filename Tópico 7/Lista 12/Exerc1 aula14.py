pessoas = []
while True:
    
    cadastrar = input("Deseja cadastrar? [S/N] ")
    if cadastrar == 'S':
        num_pessoas = int(input("Quantas pessoas você deseja cadastrar? "))
        for _ in range(num_pessoas):
            nome = input("Qual o nome da pessoa? ")
            idade = int(input("Qual a idade da pessoa? "))
            peso = float(input("Qual o peso da pessoa? "))
            pessoa = [nome, idade, peso]
            pessoas.append(pessoa)

        print(f'{len(pessoas)} pessoas cadastradas')

    else:
        maior_peso = 0
        menor_peso = 1000
        pessoas_mais_pesadas = []
        pessoas_mais_leves = []
        for pessoa in pessoas:
            if pessoa[2] > maior_peso:
                maior_peso = pessoa[2]
            if pessoa[2] < menor_peso:
                menor_peso = pessoa[2]
        for pessoa in pessoas:
            if pessoa[2] == maior_peso:
                pessoas_mais_pesadas.append(pessoa[0])
            if pessoa[2] == menor_peso:
                pessoas_mais_leves.append(pessoa[0])
        print(f"Pessoa(s) mais pesada(s): {pessoas_mais_pesadas}")
        print(f"Pessoa(s) mais leves(s): {pessoas_mais_leves}")

        pessoas_acima_20_anos = [pessoa for pessoa in pessoas if pessoa[1] > 20]
        print(f'{len(pessoas_acima_20_anos)} pessoas acima de 20 anos')
        for pessoa in pessoas_acima_20_anos:
            print(f'{pessoa[0]} tem {pessoa[1]} anos')
        print('Programa Finalizado')
        break
    
            
        
    
        
    
        