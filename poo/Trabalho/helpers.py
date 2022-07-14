# Função lista_strings_para_string: recebe uma lista de strings e retorna uma string com todas as strings separadas por vírgula
def lista_strings_para_string(lista):
    return ", ".join(lista)

# Função printa_matriz: recebe uma matriz e imprime a matriz


def printa_matriz(matriz):
    for linha in matriz:
        print(linha)

# Função check_1: recebe um número e retorna um x se o número for 1 e um espaço se o número for 0


def check_1(n):
    if n == 1:
        return "X"
    else:
        return " "


def lugares_disponiveis(matriz):
    quantidade_de_lugares_disponiveis = 0
    for linha in matriz:
        quantidade_de_lugares_disponiveis += linha.count(0)

    return quantidade_de_lugares_disponiveis


def most_empty(matrizes):
    quantidade_de_lugares_disponiveis_da_matriz_mais_vazia = 0
    for i in matrizes:
        for matriz in i:
            if matriz != []:
                if quantidade_de_lugares_disponiveis_da_matriz_mais_vazia == 0:
                    quantidade_de_lugares_disponiveis_da_matriz_mais_vazia = lugares_disponiveis(
                        matriz)
                elif lugares_disponiveis(matriz) > quantidade_de_lugares_disponiveis_da_matriz_mais_vazia:
                    quantidade_de_lugares_disponiveis_da_matriz_mais_vazia = lugares_disponiveis(
                        matriz)
    return quantidade_de_lugares_disponiveis_da_matriz_mais_vazia


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
