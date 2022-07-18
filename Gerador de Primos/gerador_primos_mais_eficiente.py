import time

# Função recursiva de MDC
def mdc(a, b):
    return a if b == 0 else mdc(b, a%b)
    
primes = []
def primo(p):

    primo = any(mdc(a, p) == 1 and (a**(p - 1)) % p == 1 for a in range(1, p))
    # Verificação de pseudoprimos
    if primo:
        multiplos = sum(p % x == 0 for x in range(2, p))
        if multiplos != 0:
            primo = False

    return primo

def gerador_primos(n):
    prime = [True for _ in range(n+1)]
    p = 2
    while p**2 <= n:
        if ((p % 2 != 0 or p == 2)) and primo(p):
            for i in range(p**2, n + 1, p):
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
