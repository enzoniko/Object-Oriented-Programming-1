x = [int(x) for x in input().split()]
y = [int(y) for y in input().split()]
compativel = all(x[i] != y[i] for i in range(5))
if compativel:
    print("Y")
else:
    print("N")

        