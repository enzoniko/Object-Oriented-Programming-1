participantes = int(input())
lista_de_presentes = {}
for _ in range(participantes):
    entrada = input().split()
    nome = entrada[0]
    presentes = [entrada[1], entrada[2], entrada[3]]
    lista_de_presentes[nome] = presentes
while True:
    entrada = input()
    if len(entrada) == 0:
        break
    nome = entrada[0]
    presente = entrada[1]

    if presente in lista_de_presentes[nome]:
        print("Uhul! Seu amigo secreto vai adorar o/")
    else:
        print("Tente Novamente!")

