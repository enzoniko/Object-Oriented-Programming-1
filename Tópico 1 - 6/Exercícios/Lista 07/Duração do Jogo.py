def duracao(inicio, fim):

    duracao = 1
    inicio += 1
    while inicio != fim:
        if inicio == 23:
            inicio = 0
        else:
            inicio += 1
        duracao += 1
    return duracao

inicio = int(input('Que horas o jogo começou? '))
fim = int(input('Que horas o jogo terminou? '))

duracao = duracao(inicio, fim)

print(f'O JOGO DUROU {duracao} horas!')
    