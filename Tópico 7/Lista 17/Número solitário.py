while True:
    tamanho_vetor = int(input())
    if tamanho_vetor == 0:
        break
    vetor = [int(x) for x in input().split()][:tamanho_vetor]
    for i in vetor:
        if vetor.count(i) % 2 != 0:
            print(i)
            break