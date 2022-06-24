x = [int(x) for x in input().split()]
y = [int(y) for y in input().split()]
compativel = True
for i in range(5):
    if x[i] == y[i]:
        compativel = False
        break
if compativel:
    print("Y")
else:
    print("N")

        