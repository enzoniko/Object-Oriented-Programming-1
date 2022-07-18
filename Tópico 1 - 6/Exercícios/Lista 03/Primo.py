num = int(input("Número: "))
multiplos = sum(num % x == 0 for x in range(2, num))
if multiplos == 0:
    print(f"{num} é primo!")
else:
    print(f"{num} não é primo!")