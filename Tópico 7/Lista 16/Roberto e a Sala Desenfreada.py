# Função que transforma a relação, fazendo cada curso ser uma chave e cada valor uma lista de matriculas que fazem parte do curso
def transformar_relacao(relacao):

    relacao_invertida = dict()

    # Pra cada matrícula na relação
    for matricula in relacao:

        # Pega o curso relacionado a matrícula
        curso = relacao[matricula]

        # Se o curso não existe, cria uma lista com a matricula
        if curso not in relacao_invertida:
            relacao_invertida[curso] = [matricula]

        # Se o curso já existe, adiciona a matricula na lista
        else:
            relacao_invertida[curso].append(matricula)

    # Retorna a relação invertida
    return relacao_invertida

# Pega o dicionario de matriculas
def matriculas_cursos():

    relacao = dict()
    num_alunos = int(input())

    # Pra cada aluno
    for i in range(num_alunos):

        entrada = input().split()

        # Pega a matrícula
        matricula = int(entrada[0])

        # Pega o curso
        curso = entrada[1]

        # Adiciona a matricula como chave e o curso como valor no dicionario de relações
        relacao[matricula] = curso
    
    # Retorna o dicionario de relações transformado
    return transformar_relacao(relacao)

# Calcula a quantidade de alunos por curso
def quantidade_de_alunos_por_curso(relacao):

    quantidade_de_alunos_por_curso = dict()
    intrusos = 0

    # Pra cada curso
    for curso in relacao:

        # Cria um dicionario com a quantidade de alunos por curso
        quantidade_de_alunos_por_curso[curso] = len(relacao[curso])
    
    # Pra cada curso nesse novo dicionario
    for curso in quantidade_de_alunos_por_curso:

        # Se o curso for EPR ou EHD
        if curso == 'EPR' or curso == 'EHD':
            
            # Printa a quantidade de alunos por curso
            print(f'{curso}: {quantidade_de_alunos_por_curso[curso]}') 
        
        # Senão, soma a quantidade de alunos por curso ao total de intrusos
        else:
            intrusos += quantidade_de_alunos_por_curso[curso]
    
    # Printa o total de intrusos
    print(f'INTRUSOS: {intrusos}')

# Roda o programa
while True:
    quantidade_de_alunos_por_curso(matriculas_cursos())
        

