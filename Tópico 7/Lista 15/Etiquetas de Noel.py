# Pega os dicionarios de traduçoes e crianças selecionadas
def pegar_dicionarios():

    quantidade_traducoes = int(input())

    # Dicionario de traduçoes
    traducoes = dict()
    for i in range(quantidade_traducoes):
        lingua = input()
        traducao = input()
        traducoes[lingua] = traducao

    quantidade_criancas = int(input())

    # Dicionario de crianças
    criancas = dict()
    for i in range(quantidade_criancas):
        nome = input()
        lingua = input()
        criancas[nome] = lingua

    # Retorna os dicionarios 
    return traducoes, criancas

# Faz cada etiqueta
def etiquetas(dicionarios):

    # Pra cada criança 
    for crianca in dicionarios[1]:

        # Printa o nome dele
        print(crianca)

        # Printa cada feliz natal
        print(dicionarios[0][dicionarios[1][crianca]])
        print()
 

etiquetas(pegar_dicionarios())
