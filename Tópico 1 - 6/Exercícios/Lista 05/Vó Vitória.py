numero_testes = 1
while True:
    depositos = int(input("Quantos depósitos você quer fazer? "))
    if depositos == 0:
        break
    print(f"Teste {numero_testes}")
    numero_testes += 1
    diferenca_anterior = 0
    for _ in range(depositos):
        cofre_j, cofre_z = [int(valor) for valor in input("Valores depositados no cofre de Joãozinho e Zezinho separados por um espaço: ").split()]

        diferenca_atual = cofre_j - cofre_z
        diferenca_nova = (
            diferenca_atual + diferenca_anterior
            if diferenca_anterior < 0
            and diferenca_atual > 0
            or diferenca_anterior >= 0
            and diferenca_anterior > 0
            else diferenca_atual - diferenca_anterior
        )

        print(diferenca_nova)
        diferenca_anterior = diferenca_nova
    print()

    