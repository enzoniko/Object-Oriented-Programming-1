tipo = int(input("Qual o tipo de combustível abastacido (1.Álcool 2.Gasolina 3.Diesel 4.Fim)? "))
quantidade_1, quantidade_2, quantidade_3 = 0,0,0
while True:
    if tipo in [1, 2, 3]:
        if tipo == 1:
            quantidade_1 += 1
        elif tipo == 2:
            quantidade_2 += 1
        else:
            quantidade_3 += 1
        tipo = int(input("Qual o tipo de combustível abastacido (1.Álcool 2.Gasolina 3.Diesel 4.Fim)? "))
    elif tipo == 4:
        break
    else:
        tipo = int(input("Qual o tipo de combustível abastacido (1.Álcool 2.Gasolina 3.Diesel 4.Fim)? "))
print("MUITO OBRIGADO")
print(f"Álcool: {quantidade_1}")
print(f"Gasolina: {quantidade_2}")
print(f"Diesel: {quantidade_3}")
    
    
   