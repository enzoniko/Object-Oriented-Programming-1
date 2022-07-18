empresa1 = set()
empresa2 = set()

empresas = [empresa1, empresa2]
while True:
    modo = int(input("\nQual operação deseja realizar?\n1 - Relação de clientes\n2 - Adicionar clientes\n3 - Clientes cadastrados nas duas empresas\n4 - Quantidade de clientes\n0 - Sair do programa\n--> "))
    if modo == 1:
        print()
        print(f'clientes matriculados em empresa1: {empresa1}')
        print(f'clientes matriculados em empresa2: {empresa2}')
    elif modo == 2:
        while True:
            cliente, empresa = list(
                input(
                    "\nDigite o nome do cliente e a empresa, separados por um espaço: \n1 - 1° empresa\n2 - 2° empresa\nDigite '0 0' para sair\n--> "
                ).split()
            )

            if empresa == '1':
                empresa1.add(cliente)
            elif empresa == '2':
                empresa2.add(cliente)
            else:
                break
    elif modo == 3:
        clientes_com_direito_a_desconto = []
        for x in empresas:
            for y in empresas:
                if x.intersection(y) and x is not y:
                    clientes_com_direito_a_desconto.extend(iter(x.intersection(y)))
        if len(clientes_com_direito_a_desconto) > 1:               
            print(f'\nclientes cadastrados nas duas empresas: {set(clientes_com_direito_a_desconto)}')

    elif modo == 4:
        clientes_com_direito_a_desconto = []
        for x in empresas:
            for y in empresas:
                if x.intersection(y) and x is not y:
                    clientes_com_direito_a_desconto.extend(iter(x.intersection(y)))
        print(f'{len(empresa1)} clientes na empresa 1')
        print(f'{len(empresa2)} clientes na empresa 2')
        print(f'{len(set(clientes_com_direito_a_desconto))} clientes em ambas as empresas')
        print(f'{len(empresa1.symmetric_difference(empresa2))} clientes em apenas 1 das empresas')
        print(f'Total de clientes: {len(empresa1.union(empresa2))}')

    else:
        print("Programa Finalizado!")
        break
    