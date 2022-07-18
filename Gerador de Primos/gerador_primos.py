import time
# Função recursiva de MDC
def mdc(a, b):
    return a if b == 0 else mdc(b, a%b)

# Função pra ver se é primo
def gerador_primos(n):
    primos = []
    for p in range(n + 1):
        primo = any(mdc(a, p) == 1 and (a**(p - 1)) % p == 1 for a in range(p))
        # Verificação de pseudoprimos
        if primo:
            multiplos = sum(p % x == 0 for x in range(2, p))
            if multiplos != 0:
                primo = False

        if primo:
            primos.append(p)

    return primos
t0 = time.time()
print(len(gerador_primos(100000)))
t1 = time.time()
print("Time required:", t1 - t0)


