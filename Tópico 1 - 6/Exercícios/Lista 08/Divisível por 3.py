while True:
    n, m = [int(x) for x in input().split()]
    m = str(m)[:n]
    soma_algarismos = sum(int(m[i]) for i in range(n))
    if soma_algarismos % 3 == 0:
        print(f'{soma_algarismos} sim')
    else:
        print(f'{soma_algarismos} não')

    continuar = input("Quer continuar? (s/n)")
    if continuar == 'n':
        break