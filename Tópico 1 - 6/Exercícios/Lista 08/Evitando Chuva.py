n = int(input())
guarda_chuvas = 0
c, e = 0, 0
d_anterior, n_anterior = '', ''
for x in range(n):
    d, n = [i for i in input().split()]
    if d == 'chuva' and d == 'sol' and x == 0:
        c += 1
    if d == 'sol' and n == 'chuva' and x == 0:
        e += 1
    if d_anterior + ' ' + n_anterior == d + ' ' + n:
        if d == 'sol' and n == 'chuva':
            e += 1
        if d == 'chuva' and n == 'sol':
            c += 1
    else:
        d_anterior = d
        n_anterior = n
            
        
    
    
    
        
print(c, e)