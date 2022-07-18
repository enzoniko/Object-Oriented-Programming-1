nota_1, nota_2, nota_3, nota_4, nota_5 = [float(x) for x in input("Notas da agremiação separadas por um espaço: ").split()]

menor_nota = 11
nome_menor_nota = ''
for _ in range (5):
    if nota_1 < menor_nota:
        menor_nota = nota_1
        nome_menor_nota = 'nota_1'
    elif nota_2 < menor_nota:
        menor_nota = nota_2
        nome_menor_nota = 'nota_2'
    elif nota_3 < menor_nota:
        menor_nota = nota_3
        nome_menor_nota = 'nota_3'
    elif nota_4 < menor_nota:
        menor_nota = nota_4
        nome_menor_nota = 'nota_4'
    elif nota_5 < menor_nota:
        menor_nota = nota_5
        nome_menor_nota = 'nota_5'

maior_nota = 4
nome_maior_nota = ''
for _ in range (5):
    if nota_1 > maior_nota:
        maior_nota = nota_1
        nome_maior_nota = 'nota_1'
    elif nota_2 > maior_nota:
        maior_nota = nota_2
        nome_maior_nota = 'nota_2'
    elif nota_3 > maior_nota:
        maior_nota = nota_3
        nome_maior_nota = 'nota_3'
    elif nota_4 > maior_nota:
        maior_nota = nota_4
        nome_maior_nota = 'nota_4'
    elif nota_5 > maior_nota:
        maior_nota = nota_5
        nome_maior_nota = 'nota_5'

soma = 0
nota_adicionada_1 = ''
nota_adicionada_2 = ''
nota_adicionada_3 = ''

for _ in range(5):
    if (
        nome_menor_nota != 'nota_1'
        and nome_maior_nota != 'nota_1'
        and nota_adicionada_1 != 'nota_1'
        and nota_adicionada_2 != 'nota_1'
        and nota_adicionada_3 != 'nota_1'
    ):
        soma += nota_1

        if nota_adicionada_1 == '':
            nota_adicionada_1 = 'nota_1'
        elif nota_adicionada_2 == '':
            nota_adicionada_2 = 'nota_1'
        elif nota_adicionada_3 == '':
            nota_adicionada_3 = 'nota_1'

    elif (
        nome_menor_nota != 'nota_2'
        and nome_maior_nota != 'nota_2'
        and nota_adicionada_1 != 'nota_2'
        and nota_adicionada_2 != 'nota_2'
        and nota_adicionada_3 != 'nota_2'
    ):
        soma += nota_2
        if nota_adicionada_1 == '':
            nota_adicionada_1 = 'nota_2'
        elif nota_adicionada_2 == '':
            nota_adicionada_2 = 'nota_2'
        elif nota_adicionada_3 == '':
            nota_adicionada_3 = 'nota_2'

    elif (
        nome_menor_nota != 'nota_3'
        and nome_maior_nota != 'nota_3'
        and nota_adicionada_1 != 'nota_3'
        and nota_adicionada_2 != 'nota_3'
        and nota_adicionada_3 != 'nota_3'
    ):
        soma += nota_3
        if nota_adicionada_1 == '':
            nota_adicionada_1 = 'nota_3'
        elif nota_adicionada_2 == '':
            nota_adicionada_2 = 'nota_3'
        elif nota_adicionada_3 == '':
            nota_adicionada_3 = 'nota_3'

    elif (
        nome_menor_nota != 'nota_4'
        and nome_maior_nota != 'nota_4'
        and nota_adicionada_1 != 'nota_4'
        and nota_adicionada_2 != 'nota_4'
        and nota_adicionada_3 != 'nota_4'
    ):
        soma += nota_4
        if nota_adicionada_1 == '':
            nota_adicionada_1 = 'nota_4'
        elif nota_adicionada_2 == '':
            nota_adicionada_2 = 'nota_4'
        elif nota_adicionada_3 == '':
            nota_adicionada_3 = 'nota_4'

    elif (
        nome_menor_nota != 'nota_5'
        and nome_maior_nota != 'nota_5'
        and nota_adicionada_1 != 'nota_5'
        and nota_adicionada_2 != 'nota_5'
        and nota_adicionada_3 != 'nota_5'
    ):
        soma += nota_5
        if nota_adicionada_1 == '':
            nota_adicionada_1 = 'nota_5'
        elif nota_adicionada_2 == '':
            nota_adicionada_2 = 'nota_5'
        elif nota_adicionada_3 == '':
            nota_adicionada_3 = 'nota_5'

print("{:.1f}".format(soma))
