# Pega a pressão desejada
N = int(input("Pressão desejada: "))

# Pega a pressão lida
M = int(input("Pressão lida: "))

# Calcula a diferença das pressões
if 1 <= N <= 40 and 1 <= M <= 40:
    print(N - M)
else:
    print("O valor de pressão é entre 1 e 40")
    