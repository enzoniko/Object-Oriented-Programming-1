mergulharam, retornaram = [int(x) for x in input().split()]
retornados = [int(x) for x in input().split()][:retornaram]
voluntarios = [int(x) for x in range(1, mergulharam + 1)]
for i in retornados:
    voluntarios.remove(i)
if not voluntarios:
    print('*')
else:
    for i in voluntarios:
        print(i, end=' ')
    