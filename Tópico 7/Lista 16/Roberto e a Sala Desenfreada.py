# Função que transforma a relação, fazendo cada curso ser uma chave e cada valor uma lista de matriculas que fazem parte do curso
def transformar_relacao(relacao):

    relacao_invertida = {}

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

    relacao = {}
    num_alunos = int(input())

    # Pra cada aluno
    for _ in range(num_alunos):
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

    intrusos = 0

    quantidade_de_alunos_por_curso = {
        curso: len(relacao[curso]) for curso in relacao
    }

    # Pra cada curso nesse novo dicionario
    for curso, value in quantidade_de_alunos_por_curso.items():

        # Se o curso for EPR ou EHD
        if curso in ['EPR', 'EHD']:

            # Printa a quantidade de alunos por curso
            print(f'{curso}: {value}') 

        else:
            intrusos += quantidade_de_alunos_por_curso[curso]

    # Printa o total de intrusos
    print(f'INTRUSOS: {intrusos}')

# Roda o programa
while True:
    quantidade_de_alunos_por_curso(matriculas_cursos())
        

