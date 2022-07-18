while True:
    entrada = [int(x) for x in input().split()]
    if not entrada:
        break
    linhas = entrada[0]
    colunas = entrada[1]

    litros = 0
    for _ in range(linhas):
        linha = [int(x) for x in input().split()][:colunas]
        litros += sum(linha)

    print(f'{litros//60} saca(s) e {litros%60} litro(s)')

