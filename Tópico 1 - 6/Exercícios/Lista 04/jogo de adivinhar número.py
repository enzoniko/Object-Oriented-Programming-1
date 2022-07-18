from random import randint
x = int(randint(0, 10))
n = int(input("Escolha um número: "))
count = 1
while n != x:
   n = int(input("Escolha um número: "))
   count += 1
print (f"Você acertou com {count} tentativas!")
