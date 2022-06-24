while True:
    matriz = list()
    linhas, colunas, posicao = [int(x) for x in input().split()]
    if linhas == colunas == posicao == 0:
        break
    else:
        for i in range(linhas):
            linha = [int(x) for x in input().split()][:colunas]
            matriz.append(linha)
        
        for linha in range(len(matriz)):
            
            nivel_ventilador_esquerda = 0
            nivel_ventilador_direita = 0
            for ventilador_esquerda in range(posicao - 2, -1, -1):
                if matriz[linha][ventilador_esquerda] != 0:
                    nivel_ventilador_esquerda = matriz[linha][ventilador_esquerda]
                    break
            for ventilador_direita in range(posicao, colunas):
                if matriz[linha][ventilador_direita] != 0:
                    nivel_ventilador_direita = matriz[linha][ventilador_direita]
                    break
            
            posicao += (nivel_ventilador_esquerda - nivel_ventilador_direita)

            if matriz[linha][posicao - 1] != 0:
                print('BOOM', linha + 1, posicao)
                break
        if matriz[linha][posicao - 1] == 0:
            print("OUT", posicao)
                 