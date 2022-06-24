m, n = [int(x) for x in input("Digite uma dupla de valores separados por espaço: ").split()]
while m > 0 and n > 0:
    soma = 0
    if m > n:
        for x in range(n, m + 1):
            soma += x
            print(x, end=" ")
    elif n > m:
        for x in range(m, n + 1):
            soma += x
            print(x, end=" ")
    print(f'sum = {soma}')
    m, n = [int(x) for x in input("Digite uma dupla de valores separados por espaço: ").split()]
    

        
            

            