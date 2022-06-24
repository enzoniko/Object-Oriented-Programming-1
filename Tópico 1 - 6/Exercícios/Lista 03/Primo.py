num = int(input("Número: "))
multiplos = 0
for x in range(2, num):
    if num % x == 0:
        multiplos += 1

if multiplos == 0:
    print(f"{num} é primo!")
else:
    print(f"{num} não é primo!")