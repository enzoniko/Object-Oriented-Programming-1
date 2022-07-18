# Enzo Nicolás Spotorno Bieger - 22100614
def segundos_ligado():
    n = int(input())
    instante_anterior = 0
    soma_das_diferencas_dos_instantes = 10
    for x in range(n):
        instante = int(input())
        if x > 0:
            soma_das_diferencas_dos_instantes += (instante - instante_anterior)
        instante_anterior = instante

    return soma_das_diferencas_dos_instantes

soma_das_diferencas_dos_instantes = segundos_ligado()

print(soma_das_diferencas_dos_instantes)
