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


'''
# Início teste
lista = ["a", "b", "c"]
print(lista_strings_para_string(lista))
# Fim teste
'''
