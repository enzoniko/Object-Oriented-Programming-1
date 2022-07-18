casos_de_teste = int(input())
for _ in range(casos_de_teste):
    provas, alunos = [int(x) for x in input().split()]
    for _ in range(alunos):
        notas_aluno = [float(x) for x in input().split()][:provas]
        print(round((sum(notas_aluno) / provas), 2))
        
    
