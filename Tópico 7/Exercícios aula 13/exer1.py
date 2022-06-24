fut = set()
bas = set()
nat = set()
vol = set()
modalidades = [fut, bas, nat, vol]
while True:
    modo = int(input("\nQual operação deseja realizar?\n1 - Relação de matriculados\n2 - Adicionar alunos\n3 - Alunos com direito ao desconto\n4 - Quantidade de alunos por modalidade e total\n0 - Sair do programa\n--> "))
    if modo == 1:
        print()
        print(f'Alunos matriculados em futebol: {fut}')
        print(f'Alunos matriculados em basquete: {bas}')
        print(f'Alunos matriculados em natação: {nat}')
        print(f'Alunos matriculados em vôlei: {vol}')
    elif modo == 2:
        while True:
            aluno, modalidade = [x for x in input("\nDigite o nome do aluno e a modalidade, separados por um espaço: \n1 - futebol\n2 - basquete\n3 - natação\n4 - vôlei\nDigite '0 0' para sair\n--> ").split()]
            if modalidade == '1':
                fut.add(aluno)
            elif modalidade == '2':
                bas.add(aluno)
            elif modalidade == '3':
                nat.add(aluno)
            elif modalidade == '4':
                vol.add(aluno)
            else:
                break
            
    elif modo == 3:
        alunos_com_direito_a_desconto = []
        for x in modalidades:
            for y in modalidades:
                if x.intersection(y) and x is not y:
                    for i in x.intersection(y):
                        alunos_com_direito_a_desconto.append(i)
        if len(alunos_com_direito_a_desconto) > 1:               
            print(f'Alunos com direito à desconto: {set(alunos_com_direito_a_desconto)}')
         
    elif modo == 4:
        print(f'{len(fut)} alunos matriculados em futebol')
        print(f'{len(bas)} alunos matriculados em basquete')
        print(f'{len(nat)} alunos matriculados em natação')
        print(f'{len(vol)} alunos matriculados em vôlei')
        
        print(f'Total de alunos: {len(fut.union(bas).union(nat).union(vol))}')
        
    else:
        print("Programa Finalizado!")
        break
    
    
    
