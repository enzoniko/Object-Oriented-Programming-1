while True:
    assinaturas = {}
    print('----------------------------------------------------')
    alunos = int(input())
    assinaturas_falsas = 0
    if alunos == 0:
        break
    for _ in range(alunos):
        entrada = input().split()
        nome = entrada[0]
        assinatura_original = entrada[1]
        assinaturas[nome] = assinatura_original
    alunos_presentes = int(input())
    for _ in range(alunos_presentes):
        entrada = input().split()
        nome = entrada[0]
        assinatura_sala = entrada[1]
        if assinaturas[nome] != assinatura_sala:
            assinaturas_falsas += 1
    print(assinaturas_falsas)
    
        
