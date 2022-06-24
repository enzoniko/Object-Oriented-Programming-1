import time
# Função recursiva de MDC
def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a%b)

# Função pra ver se é primo
def gerador_primos(n):
    primos = []
    for p in range(n + 1):
        primo = False

        # Teorema de Fermat
        for a in range(p):
            if mdc(a, p) == 1 and (a**(p - 1)) % p == 1:
                primo = True
                break
        # Verificação de pseudoprimos
        if primo == True:
            multiplos = 0
            for x in range(2, p):
                if p % x == 0:
                    multiplos += 1
            if multiplos != 0:
                primo = False
 
        if primo == True:
            primos.append(p)
     
    return primos
t0 = time.time()
print(len(gerador_primos(100000)))
t1 = time.time()
print("Time required:", t1 - t0)


