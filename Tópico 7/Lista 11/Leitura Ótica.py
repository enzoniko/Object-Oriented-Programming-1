alternativas = ['A', 'B', 'C', 'D', 'E']

def corretamente_preenchida(resposta):
    respostas_preenchidas = [
        alternativas[resposta.index(r)] for r in resposta if r <= 127
    ]

    return respostas_preenchidas[0] if len(respostas_preenchidas) == 1 else '*'
        
while True:
    questoes = int(input())
    for _ in range(questoes):
        print(corretamente_preenchida([int(x) for x in input().split()]))

    if questoes == 0:
        break
    