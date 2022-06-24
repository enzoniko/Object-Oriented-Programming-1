x = int(input("Segundos que o piloto mais rápido demora para completar uma volta: "))
y = int(input("Segundos que o piloto mais lento demora para completar uma volta: "))
diferenca = y - x

while diferenca < y:
    diferenca += diferenca
else:
    voltas = diferenca / (y - x)
print(int(voltas))
    
    
