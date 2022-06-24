def passa_pela_porta():
    profundidade_colchao, altura_colchao, largura_colchao = [int(dimensao) for dimensao in input("Digite as dimensões do colchão separadas por um espaço: ").split()]
    altura_porta, largura_porta = [int(dimensao) for dimensao in input("Digite as dimensões da porta separadas por um espaço: ").split()]
    if (altura_colchao <= altura_porta or altura_colchao <= largura_porta) or (largura_colchao <= altura_porta or largura_colchao <= largura_porta):
        return 'S'
    else:
        return 'N'
    
if passa_pela_porta() == 'S':
    print("Você escolheu um colchão adequado! Parabéns pela compra!")
else:
    print("Você precisa escolher um colchão com outras dimensões!")


