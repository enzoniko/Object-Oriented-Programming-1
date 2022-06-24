altura_pulo, canos = [int(x) for x in input().split()]
alturas_canos = [int(x) for x in input().split()][:canos]
winnable = True
for cano in range(1, len(alturas_canos)):
    
    if altura_pulo < abs(alturas_canos[cano] - alturas_canos[cano - 1]):
        winnable = False

if winnable:
    print("YOU WIN")
else:
    print("YOU LOSE")