def criar_lista_com_3_notas():
    notas = []
    while len(notas) <= 2:
        nota = int(input())
        if nota <= 10 and nota >= 0:
            notas.append(nota)
    return notas

def media_notas(notas):
    soma = sum(notas[i] for i in range(len(notas)))
    return soma/len(notas)

def maior_nota(notas):
    nota_maior = 0
    for i in range(len(notas)):
        if notas[i] >= nota_maior:
            nota_maior = notas[i]
    return nota_maior

def menor_nota(notas):
    nota_menor = 10
    for i in range(len(notas)):
        if notas[i] <= nota_menor:
            nota_menor = notas[i]
    return nota_menor
notas = criar_lista_com_3_notas()
print(f"A média do aluno é: {media_notas(notas)}")
print(f"A maior nota do aluno é: {maior_nota(notas)}")
print(f"A menor nota do aluno é: {menor_nota(notas)}")
print(f"A diferença entre a maior e a menor nota do aluno é: {maior_nota(notas) - menor_nota(notas)}")