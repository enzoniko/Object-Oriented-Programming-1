vetor = [int(input())]
vetor.extend(2 * vetor[i-1] for i in range(1, 10))
for i in range(len(vetor)):
    print(f"N[{i}] = {vetor[i]}")