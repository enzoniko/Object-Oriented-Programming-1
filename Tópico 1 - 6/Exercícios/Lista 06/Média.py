def media():
    soma = 0
    melhor_nota = 0
    for aluno in range (1, 6):
        nota = float(input(f"Nota {aluno}:"))
        soma += nota
        if nota > melhor_nota:
            melhor_nota = nota
    media = soma / 5
    return media, melhor_nota

media, melhor_nota = media()
if melhor_nota >= 5.75:
    print("APROVADO")
elif melhor_nota >= 2.75:
    print("EM RECUPERAÇÃO")
else:
    print("REPROVADO")

