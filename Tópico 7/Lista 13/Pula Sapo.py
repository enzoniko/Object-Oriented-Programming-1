altura_pulo, canos = [int(x) for x in input().split()]
alturas_canos = [int(x) for x in input().split()][:canos]
winnable = all(
    altura_pulo >= abs(alturas_canos[cano] - alturas_canos[cano - 1])
    for cano in range(1, len(alturas_canos))
)

if winnable:
    print("YOU WIN")
else:
    print("YOU LOSE")