n, m = [int(x) for x in input().split()]

primo_n = 0
for i in range(n + 1):
    divisores = 0
    for divisor in range(2, i):
        if i % divisor == 0:
            divisores += 1
    if divisores == 0:
        primo_n = i
            
primo_m = 0
for i in range(m + 1):
    divisores = 0
    for divisor in range(2, i):
        if i % divisor == 0:
            divisores += 1
    if divisores == 0:
        primo_m = i
            
print(primo_m * primo_n)
