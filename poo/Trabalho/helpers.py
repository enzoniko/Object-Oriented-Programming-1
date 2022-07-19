# Função lista_strings_para_string: recebe uma lista de strings e retorna uma string com todas as strings separadas por vírgula
def lista_strings_para_string(lista):
    return ", ".join(lista)

# Função printa_matriz: recebe uma matriz e imprime a matriz


def printa_matriz(matriz):
    for linha in matriz:
        print(linha)

# Função check_1: recebe um número e retorna um x se o número for 1 e um espaço se o número for 0


def check_1(n):
    return "X" if n == 1 else " "

# Função lugares_disponiveis: recebe uma matriz e retorna o número de lugares disponíveis na matriz


def lugares_disponiveis(matriz):
    return sum(linha.count(0) for linha in matriz)

# Função most_empty: recebe uma lista de salas e retorna a sala com mais lugares disponíveis


def most_empty(matrizes):
    quantidade_de_lugares_disponiveis_da_matriz_mais_vazia = 0
    for i in matrizes:
        for matriz in i:
            if matriz != [] and (quantidade_de_lugares_disponiveis_da_matriz_mais_vazia == 0 or quantidade_de_lugares_disponiveis_da_matriz_mais_vazia != 0 and lugares_disponiveis(matriz) > quantidade_de_lugares_disponiveis_da_matriz_mais_vazia):
                quantidade_de_lugares_disponiveis_da_matriz_mais_vazia = lugares_disponiveis(
                    matriz)
    return quantidade_de_lugares_disponiveis_da_matriz_mais_vazia


# DEIXAR PRA O AMOR DA MINHA VIDA EXPLICAR A FUNCAO
def verificador_input(coisa, lista, condicao, mensagem_erro):
    while True:
        numero = int(
            input(f"Digite o número {coisa} que você deseja: "))
        if (condicao == 'in' and numero - 1 in range(len(lista))) or (condicao == '<=' and numero <= lista[0] and numero > 0):
            return numero
        else:
            print(mensagem_erro)


'''
# Início teste
lista = ["a", "b", "c"]
print(lista_strings_para_string(lista))

matrizes = [[[0, 0, 1, 1], [0, 0, 0, 0]], [[0, 0, 1, 1], [0, 0, 1, 0]]]
for matriz in matrizes:
    if lugares_disponiveis(matriz) == most_empty(matrizes):
        print(matriz)
# Fim teste
'''
