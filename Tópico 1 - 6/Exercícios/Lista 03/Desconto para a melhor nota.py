melhor_nota = 0
for _ in range(5):
    nome = input("Nome: ")
    nota = float(input("Média geral: "))
    mensalidade = float(input("Valor da mensalidade: "))
    if nota > melhor_nota:
        melhor_nota = nota
        melhor_nome = nome
        melhor_mensalidade = mensalidade

mensalidade_com_desconto = melhor_mensalidade - melhor_mensalidade * 0.3
print (f"{melhor_nome} teve a melhor nota. Sua mensalidade vai de {melhor_mensalidade} para {mensalidade_com_desconto}")


        
    

    
    