alternativas = ['A', 'B', 'C', 'D', 'E']

def corretamente_preenchida(resposta):
    respostas_preenchidas = []
    for r in resposta:
        if r <= 127:
            respostas_preenchidas.append(alternativas[resposta.index(r)])
    if len(respostas_preenchidas) == 1:
        return respostas_preenchidas[0]
    else:
        return '*'
        
while True:
    questoes = int(input())
    for q in range(questoes):
        print(corretamente_preenchida([int(x) for x in input().split()]))
        
    if questoes == 0:
        break
    