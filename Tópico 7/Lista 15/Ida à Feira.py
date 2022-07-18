# Recebe o dicionario de produtos disponíveis e o dicionario de produtos desejados
def ida_a_feira():
    
    # Dicionario de produtos disponiveis
    quantidade_produtos_disponiveis = int(input())
    produtos_disponiveis = {}
    for _ in range(quantidade_produtos_disponiveis):
        produto_disponivel = input().split()
        produtos_disponiveis[produto_disponivel[0]] = float(produto_disponivel[1])

    # Dicionario de produtos desejados
    quantidade_produtos_desejados = int(input())
    produtos_desejados = {}
    for _ in range(quantidade_produtos_desejados):
        produto_desejado = input().split()
        produtos_desejados[produto_desejado[0]] = int(produto_desejado[1])

    # Retorna ambos os dicionarios
    return produtos_disponiveis, produtos_desejados

# Calcula o valor total da compra
def calcular_preco_total(dicionarios):

    return sum(
        dicionarios[0][produto_desejado] * dicionarios[1][produto_desejado]
        for produto_desejado in dicionarios[1].keys()
        if produto_desejado in dicionarios[0].keys()
    )

# Pra cada compra, calcula o valor total da compra
for _ in range( int(input())):
    print('R$ {:.2f}'.format(calcular_preco_total(ida_a_feira())))


