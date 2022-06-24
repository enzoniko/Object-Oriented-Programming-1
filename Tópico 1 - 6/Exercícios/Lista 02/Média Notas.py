# Lê três notas do usuário
nota1, nota2, nota3 = input("Digite as 3 notas separadas por um espaço: ").split()

# Calcula a média das notas
media = (float(nota1) + float(nota2) + float(nota3)) / 3

# Se a média for abaixo de 5
if media < 5:
    
    # Fala que o usuário foi reprovado
    print("Você foi reprovado!")

# Se a média estiver entre 5 e 7
elif 5 <= media < 7:
    
    # Fala que o usuário está em recuperação
    print("Você está em recuperação!")

# Se a média for maior ou igual a 7
else:
    
    # Fala que o usuário foi aprovado
    print("Você foi aprovado!")
    
