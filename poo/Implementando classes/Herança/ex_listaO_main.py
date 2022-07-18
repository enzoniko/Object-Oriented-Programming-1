'''
Exemplo de como criar uma lista de objetos (inserir, alterar, consultar, excluir)

Criar um cadastro de funcionário
- ID
- Nome do funcionário
- CPF
- Sexo

Main possui um menu
- Inserir funcionário
- Alterar informação do funcionário
- Consultar pelo nome ou cpf ou ID
- Excluir funcionário

Cada funcionário é inserido em uma lista de objetos
'''

from ex_listaO_funcionario import Funcionario

idF = 1

flag=False

f = Funcionario(str(idF), 'João', '123.456.789-10', 'M') # cria uma instância de Funcionário
funcionarios = [f]
while True:
    print('Menu de funcionários')
    print('Escolha uma operação para realizar: ')
    print('1 - Cadastrar funcionário')
    print('2 - Alterar informação de funcionário')
    print('3 - Consultar (nome, cpf ou ID)')
    print('4 - Excluir funcionário')
    print('5 - Encerrar execução')
    op = int(input('Escolha uma operação: ')) # o usuário escolhe a opção

    if op == 1: # Operação 1 - Cadastrar
        print('Cadastro de funcionário')

        idF += 1
        nome = str(input('Nome: '))
        cpf = str(input('CPF: '))
        sexo = str(input('Sexo: '))

        f = Funcionario('', '', '', '') # cria o objeto Funcionario
        f.set_id(str(idF))
        f.set_nome(nome)
        f.set_cpf(cpf)
        f.set_sexo(sexo)

        funcionarios.append(f)  # adiciona na lista de funcionários

    elif op == 2: # Operação 2 - Alterar (pelo ID)
        print('Alterar informação de usuário')
        idF = str(input('Digite o ID do funcionário: '))

        for func in funcionarios:  # percorre a lista de funcionários
            if idF == func.get_id():  # busca pelo ID do funcionário a ser alterado
                print('Digite as novas informações do usuário')
                nome = str(input('Nome: '))
                cpf = str(input('CPF: '))
                sexo = str(input('Sexo: '))

                func.set_nome(nome) # altera os dados do funcionário
                func.set_cpf(cpf)
                func.set_sexo(sexo)

    elif op == 3: # Operação 3 - Consultar
        print('Consultar funcionário')
        print('1 - Consultar pelo ID')
        print('2 - Consultar pelo nome')
        print('3 - Consultar pelo CPF')
        consulta = int(input('Escolha a forma de consulta: '))

        if consulta == 1: # Consultar pelo ID
            c = str(input('Digite o ID: '))
            for func in funcionarios:
                if c == func.get_id():
                    print('ID:', func.get_id())  # resgata os dados do funcionário
                    print('Nome:', func.get_nome())
                    print('CPF:', func.get_cpf())
                    print('Sexo:', func.get_sexo())


        elif consulta == 2: # Consultar pelo Nome
            c = str(input('Digite o nome: '))
            for func in funcionarios:
                if c == func.get_nome():
                    print('ID:', func.get_id())  # resgata os dados do funcionário
                    print('Nome:', func.get_nome())
                    print('CPF:', func.get_cpf())
                    print('Sexo:', func.get_sexo())

        else:  # consultar pelo CPF
            c = str(input('Digite o CPF: '))
            for func in funcionarios:
                if c == func.get_cpf():
                    print('ID:', func.get_id())  # resgata os dados do funcionário
                    print('Nome:', func.get_nome())
                    print('CPF:', func.get_cpf())
                    print('Sexo:', func.get_sexo())

    elif op == 4: # Excluir funcionário (pelo ID)
        print('Excluir funcionário')
        idF = str(input('Digite o ID do funcionário: '))

        for i, j in enumerate(funcionarios): # percorre a lista de funcionários
            if idF == j.get_id():
                funcionarios.pop(i)
                print("Exclusão efetuada com sucesso!")
                flag=True
        if flag == False:
            print("Id não cadastrado!")
    else:
        break
