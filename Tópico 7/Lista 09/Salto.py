# Início das Funções
def media_saltos(saltos):
    soma = 0
    for i in range(len(saltos)):
        soma += saltos[i]
        
    return soma/len(saltos)

def maior_salto(saltos):
    salto_maior = 0
    for i in range(len(saltos)):
        if saltos[i] >= salto_maior:
            salto_maior = saltos[i]
    return salto_maior

def menor_salto(saltos):
    salto_menor = 10
    for i in range(len(saltos)):
        if saltos[i] <= salto_menor:
            salto_menor = saltos[i]
    return salto_menor

def performance_atleta(nome):
    
    numeros_cardinais = ("Primeiro", "Segundo", "Terceiro", "Quarto", "Quinto")
    saltos = []
    for i in range(5):
        saltos.append(float(input(f"{numeros_cardinais[i]} Salto: ")))
    menor = menor_salto(saltos)
    maior = maior_salto(saltos)
    saltos.remove(menor)
    saltos.remove(maior)
    print()
    print(f"Melhor salto: {maior}")
    print(f"Pior salto: {menor}")
    print("Média dos demais saltos: {:.1f}".format(media_saltos(saltos)))
    print()
    print("Resultado final:")
    print("        {}: {:.1f}".format(nome, media_saltos(saltos)))
# Fim das Funções

while True:
    nome = input("Atleta: ")
    if nome == "O":
        print("Programa Finalizado")
        break
    else:
        performance_atleta(nome)
        
    
    
    