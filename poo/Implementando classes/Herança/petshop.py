from cachorro import Cachorro
from cachorro_vip import CachorroVip

# Lista de cachorros
cachorros = list()
# ADICIONAR FUNCIONALIDADE DE SER VIP
while True:
    print('Menu do PetShop')
    print()
    print('Escolha uma operação para realizar: ')
    print('1 - Cadastrar Pet')
    print('2 - Alterar informação do Pet')
    print('3 - Consultar (nome do Pet ou nome do dono')
    print('4 - Excluir cadastro do Pet')
    print('5 - Consultar se o Pet tem restrição Alimentar')
    print('6 - Verificar qual Pet é mais idoso')
    print('7 - Encerrar execução')
    print('-----------------------------------------------------')
    operacao = int(input('Escolha uma operação: '))
    print('-----------------------------------------------------')

    if operacao == 1:
        print('Cadastro do Pet')
        print()
        raca = str(input('Raça: '))
        cor = str(input('Cor: '))
        peso = float(input('Peso: '))
        idade = int(input('Idade: '))
        nome_animal = str(input('Nome do Pet: '))
        nome_dono = str(input('Nome do dono: '))
        cachorro = Cachorro(raca, cor, peso, idade, nome_animal, nome_dono)
        cachorros.append(cachorro)
        print('-----------------------------------------------------') 
        print('Cadastro realizado com sucesso!')
        print('Informações do Pet cadastrado: ')
        print('Raça:', cachorro.get_raca())
        print('Cor:', cachorro.get_cor())
        print('Peso:', cachorro.get_peso())
        print('Idade:', cachorro.get_idade())
        print('Nome do Pet:', cachorro.get_nome_animal())
        print('Nome do dono:', cachorro.get_nome_dono())
        print('-----------------------------------------------------')
        
    elif operacao == 2:
        print('Alterar informação do Pet')
        print()
        nome_animal = str(input('Nome do Pet: '))
        print()
        for cachorro in cachorros:
            if nome_animal == cachorro.get_nome_animal():
                cachorro.set_raca(str(input('Raça: ')))
                cachorro.set_cor(str(input('Cor: ')))
                cachorro.set_peso(float(input('Peso: ')))
                cachorro.set_idade(int(input('Idade: ')))
                cachorro.set_nome_animal(str(input('Nome do Pet: ')))
                cachorro.set_nome_dono(str(input('Nome do dono: ')))
                print('-----------------------------------------------------')
                print('Informações do Pet alteradas com sucesso!')
                print('Informações do Pet alteradas: ')
                print('Raça:', cachorro.get_raca())
                print('Cor:', cachorro.get_cor())
                print('Peso:', cachorro.get_peso())
                print('Idade:', cachorro.get_idade())
                print('Nome do Pet:', cachorro.get_nome_animal())
                print('Nome do dono:', cachorro.get_nome_dono())
                print('-----------------------------------------------------')
                
            elif nome_animal not in [cachorro.get_nome_animal() for cachorro in cachorros]:
                print('Não foi encontrado nenhum animal com o nome informado!')
                print('-----------------------------------------------------')

    elif operacao == 3: # Operação 3 - Consultar
            print('Consultar Pet')
            print()
            print('1 - Consultar pelo nome do Pet')
            print('2 - Consultar pelo nome do dono')
            print('-----------------------------------------------------')
            consulta = int(input('Escolha a forma de consulta: '))
            
            if consulta == 1: 
                print('Consultar o Pet pelo seu nome')
                print('-----------------------------------------------------')
                nome_animal = str(input('Digite o nome do Pet: '))
                for cachorro in cachorros:
                    if nome_animal == cachorro.get_nome_animal():
                        print('Nome do animal:', cachorro.get_nome_animal())
                        print('Raça:', cachorro.get_raca())
                        print('Cor:', cachorro.get_cor())
                        print('Peso:', cachorro.get_peso())
                        print('Idade:', cachorro.get_idade())
                        print('Nome do dono:', cachorro.get_nome_dono())
                        print('-----------------------------------------------------')
                
                    elif nome_animal not in [cachorro.get_nome_animal() for cachorro in cachorros]:
                        print('Não foi encontrado nenhum animal com o nome informado!')
                        print('-----------------------------------------------------')
                    
                        
            elif consulta == 2:
                print('Consultar o Pet pelo nome do dono')
                print('-----------------------------------------------------')
                nome_dono = str(input('Digite o nome do dono: '))
                for cachorro in cachorros:
                    if nome_dono == cachorro.get_nome_dono():
                        print('Nome do animal:', cachorro.get_nome_animal())
                        print('Raça:', cachorro.get_raca())
                        print('Cor:', cachorro.get_cor())
                        print('Peso:', cachorro.get_peso())
                        print('Idade:', cachorro.get_idade())
                        print('Nome do dono:', cachorro.get_nome_dono())
                        print('-----------------------------------------------------')
            
                    elif nome_dono not in [cachorro.get_nome_animal() for cachorro in cachorros]:
                        print('Não foi encontrado nenhum animal com o nome informado!')
                        print('-----------------------------------------------------')

    elif operacao == 4:
        print('Excluir cadastro do Pet')
        print()
        nome_animal = str(input('Nome do Pet: '))
        for cachorro in cachorros:
            if nome_animal == cachorro.get_nome_animal():
                cachorros.remove(cachorro)
                print('Cadastro excluído com sucesso!')
                print('-----------------------------------------------------')
            elif nome_animal not in [cachorro.get_nome_animal() for cachorro in cachorros]:
                print('Não foi encontrado nenhum animal com o nome informado!')
                print('-----------------------------------------------------')

    elif operacao == 5:
        print('Verificar se o Pet tem restrição Alimentar')
        print()
        nome_animal = str(input('Nome do Pet: '))
        for cachorro in cachorros:
            if nome_animal == cachorro.get_nome_animal():
                if cachorro.get_restricao() == True:
                    print('O Pet tem restrição Alimentar!')
                    print('-----------------------------------------------------')
                    
                else:
                    print('O Pet não tem restrição Alimentar!')
                    print('-----------------------------------------------------')
            elif nome_animal not in [cachorro.get_nome_animal() for cachorro in cachorros]:
                    print('Não foi encontrado nenhum animal com o nome informado!')
                    print('-----------------------------------------------------')
        
    elif operacao == 6:
        print("Verificar qual Pet é mais idoso")
        print()
        for cachorro in cachorros:
            if cachorro.get_idade() == max([cachorro.get_idade() for cachorro in cachorros]):
                print('Nome do animal:', cachorro.get_nome_animal())
                print('Raça:', cachorro.get_raca())
                print('Cor:', cachorro.get_cor())
                print('Peso:', cachorro.get_peso())
                print('Idade:', cachorro.get_idade())
                print('Nome do dono:', cachorro.get_nome_dono())
                print('-----------------------------------------------------')

    elif operacao == 8:
        print('Sair do programa')
        print('-----------------------------------------------------')
        print('Obrigado por utilizar o nosso sistema!')
        break
                