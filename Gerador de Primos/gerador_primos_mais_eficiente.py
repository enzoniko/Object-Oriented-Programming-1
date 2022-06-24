import time

# Função recursiva de MDC
def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a%b)
    
primes = []
def primo(p):

    primo = False

    # Teorema de Fermat
    for a in range(1, p):
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
        
    return primo

def gerador_primos(n):
    prime = [True for i in range(n+1)]
    p = 2
    while(p * p <= n):
        if (p % 2 != 0 or p == 2):
            if primo(p):
                for i in range(p * p, n + 1, p):
                    prime[i] = False
        p += 1

    for p in range(2, n):
        if prime[p]:
            primes.append(p)
    return primes

t0 = time.time()
gerador_primos(100000)
print(primes)
print(len(primes))
t1 = time.time()
print("Time required:", t1 - t0)
