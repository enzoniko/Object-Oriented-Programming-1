# Enzo Nicolás Spotorno Bieger - 22100614
PA = 300
PP = 1500
PC = 600
PM = 1000
PI = 150
while True:
    gramas = 225
    a, p, c, m, i = [int(x) for x in input("Entrada: ").split()]
    gramas += ((a*PA) + (p*PP) + (c*PC) + (m*PM) + (i*PI))
    print(f"Saída: {gramas}")
    continuar = input("Deseja continuar executando? [S/N]")
    if continuar.upper() == 'N':
        break

