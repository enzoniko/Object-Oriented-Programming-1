numero_testes = 1
while True:
    depositos = int(input("Quantos depósitos você quer fazer? "))
    if depositos == 0:
        break
    print(f"Teste {numero_testes}")
    numero_testes += 1
    diferenca_anterior = 0
    for numero_deposito in range(depositos):
        cofre_j, cofre_z = [int(valor) for valor in input("Valores depositados no cofre de Joãozinho e Zezinho separados por um espaço: ").split()]
        
        diferenca_atual = cofre_j - cofre_z
        if diferenca_anterior < 0:
            if diferenca_atual > 0:
                diferenca_nova = diferenca_atual + diferenca_anterior
            else:
                diferenca_nova = diferenca_atual - diferenca_anterior
        else:
            if diferenca_anterior > 0:
                diferenca_nova = diferenca_atual + diferenca_anterior
            else:
                diferenca_nova = diferenca_atual - diferenca_anterior
        print(diferenca_nova)
        diferenca_anterior = diferenca_nova
    print()

    