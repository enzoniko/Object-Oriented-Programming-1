n = int(input('Quantos números da sequências de Fibonacci você quer mostrar? '))
x = 0
y = 1
count = 0
print (x)
print (y)
while count < n - 2:
    x = x + y
    y = x + y
    print (x)
    count += 1
    if count < n - 2:
        print (y)
        count += 1
   
    
    

    
    
