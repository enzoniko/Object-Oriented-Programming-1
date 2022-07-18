melhor_nota = 0
soma_medias = 0
for _ in range(5):
    nome = input("Nome: ")
    nota = float(input("Média geral: "))
    soma_medias += nota
    if nota > melhor_nota:
        melhor_nota = nota
        melhor_nome = nome


print("Média dos alunos: ", soma_medias / 5)
print (f"{melhor_nome} teve a melhor nota.")
if melhor_nota >= 5.75:
    print("O aluno foi aprovado!")
elif melhor_nota >= 2.75:
    print("O aluno tem o direito de fazer uma prova de recuperação")
else:
    print("O aluno foi reprovado!")

        
    
