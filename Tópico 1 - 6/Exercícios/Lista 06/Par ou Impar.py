def par_ou_impar(num):
    return 'par' if num % 2 == 0 else 'impar'
pares = 0
impares = 0
for _ in range(10):
    numero = int(input("Digite um número: "))
    if par_ou_impar(numero) == 'par':
        pares += 1
    else:
        impares += 1
print(f'{pares} números pares')
print(f'{impares} números impares')
        