x, y = [int(i) for i in input("Digite uma dupla de valores separados por espaço: ").split()]
while x != y:
    if x > y:
        print("Decrescente")
    elif x < y:
        print("Crescente")
        
    x, y = [int(i) for i in input("Digite uma dupla de valores separados por espaço: ").split()]
