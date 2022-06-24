while True:
    n, m = [int(x) for x in input().split()]
    soma_algarismos = 0
    m = str(m)[:n]
    for i in range(n):
        soma_algarismos += int(m[i])
        
    if soma_algarismos % 3 == 0:
        print(f'{soma_algarismos} sim')
    else:
        print(f'{soma_algarismos} não')
        
    continuar = input("Quer continuar? (s/n)")
    if continuar == 'n':
        break