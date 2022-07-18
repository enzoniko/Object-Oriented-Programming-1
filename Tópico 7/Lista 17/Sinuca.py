n = int(input())
primeira_fileira = [int(x) for x in input().split()][:n]
fileiras = [primeira_fileira]
for fileira_anterior in range(n):
    fileiras.append([])
    for bola in range(n - 1):
        if fileiras[fileira_anterior][bola] != fileiras[fileira_anterior][bola + 1]:
            fileiras[fileira_anterior + 1].append(-1)
        if fileiras[fileira_anterior][bola] == fileiras[fileira_anterior][bola + 1]:
            fileiras[fileira_anterior + 1].append(1)
    n -= 1

if fileiras[len(fileiras) - 2] == [-1]:
    print("branca")
if fileiras[len(fileiras) - 2] == [1]:
    print("preta")
    

