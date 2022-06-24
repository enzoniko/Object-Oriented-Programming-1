vitorias_time_A = 0
vitorias_time_B = 0
vitorias_time_C = 0
vitorias_time_D = 0
vitorias_time_E = 0
vitorias_time_F = 0
vitorias_time_G = 0
vitorias_time_H = 0
vitorias_time_I = 0
vitorias_time_J = 0
vitorias_time_K = 0
vitorias_time_L = 0
vitorias_time_M = 0
vitorias_time_N = 0
vitorias_time_O = 0
vitorias_time_P = 0

for game in range(1, 16):
    gols_1, gols_2 = [int(gols) for gols in input("Gols de cada time separados por um espaço: ").split()]
    
    if game == 1:
        if gols_1 > gols_2:
            vitorias_time_A += 1
        else:
            vitorias_time_B += 1
    elif game == 2:
        if gols_1 > gols_2:
            vitorias_time_C += 1
        else:
            vitorias_time_D += 1
    elif game == 3:
        if gols_1 > gols_2:
            vitorias_time_E += 1
        else:
            vitorias_time_F += 1
    elif game == 4:
        if gols_1 > gols_2:
            vitorias_time_G += 1
        else:
            vitorias_time_H += 1
    elif game == 5:
        if gols_1 > gols_2:
            vitorias_time_I += 1
        else:
            vitorias_time_J += 1
    elif game == 6:
        if gols_1 > gols_2:
            vitorias_time_K += 1
        else:
            vitorias_time_L += 1
    elif game == 7:
        if gols_1 > gols_2:
            vitorias_time_M += 1
        else:
            vitorias_time_N += 1
    elif game == 8:
        if gols_1 > gols_2:
            vitorias_time_O += 1
        else:
            vitorias_time_P += 1
            
    elif game == 9:
        if gols_1 > gols_2:
            if vitorias_time_A == 1:
                vitorias_time_A += 1
            else:
                vitorias_time_B += 1
        else:
            if vitorias_time_C == 1:
                vitorias_time_C += 1
            else:
                vitorias_time_D += 1
    elif game == 10:
        if gols_1 > gols_2:
            if vitorias_time_E == 1:
                vitorias_time_E += 1
            else:
                vitorias_time_F += 1
        else:
            if vitorias_time_G == 1:
                vitorias_time_G += 1
            else:
                vitorias_time_H += 1
    elif game == 11:
        if gols_1 > gols_2:
            if vitorias_time_I == 1:
                vitorias_time_I += 1
            else:
                vitorias_time_J += 1
        else:
            if vitorias_time_K == 1:
                vitorias_time_K += 1
            else:
                vitorias_time_L += 1
    elif game == 12:
        if gols_1 > gols_2:
            if vitorias_time_M == 1:
                vitorias_time_M += 1
            else:
                vitorias_time_N += 1
        else:
            if vitorias_time_O == 1:
                vitorias_time_O += 1
            else:
                vitorias_time_P += 1
                
    elif game == 13:
        if gols_1 > gols_2:
            if vitorias_time_A == 2:
                vitorias_time_A += 1
            elif vitorias_time_B == 2:
                vitorias_time_B += 1
            elif vitorias_time_C == 2:
                vitorias_time_C += 1
            elif vitorias_time_D == 2:
                vitorias_time_D += 1
                
        elif gols_1 < gols_2:
            if vitorias_time_E == 2:
                vitorias_time_E += 1
            elif vitorias_time_F == 2:
                vitorias_time_F += 1
            elif vitorias_time_G == 2:
                vitorias_time_G += 1
            elif vitorias_time_H == 2:
                vitorias_time_H += 1
                
    elif game == 14:
        if gols_1 > gols_2:
            if vitorias_time_I == 2:
                vitorias_time_I += 1
            elif vitorias_time_J == 2:
                vitorias_time_J += 1
            elif vitorias_time_K == 2:
                vitorias_time_K += 1
            elif vitorias_time_L == 2:
                vitorias_time_L += 1
                
        elif gols_1 < gols_2:
            if vitorias_time_M == 2:
                vitorias_time_M += 1
            elif vitorias_time_N == 2:
                vitorias_time_N += 1
            elif vitorias_time_O == 2:
                vitorias_time_O += 1
            elif vitorias_time_P == 2:
                vitorias_time_P += 1
                
    elif game == 15:
        if gols_1 > gols_2:
            if vitorias_time_A == 3:
                vitorias_time_A += 1
            elif vitorias_time_B == 3:
                vitorias_time_B += 1
            elif vitorias_time_C == 3:
                vitorias_time_C += 1
            elif vitorias_time_D == 3:
                vitorias_time_D += 1
            elif vitorias_time_E == 3:
                vitorias_time_E += 1
            elif vitorias_time_F == 3:
                vitorias_time_F += 1
            elif vitorias_time_G == 3:
                vitorias_time_G += 1
            elif vitorias_time_H == 3:
                vitorias_time_H += 1
                
        elif gols_1 < gols_2:
            if vitorias_time_I == 3:
                vitorias_time_I += 1
            elif vitorias_time_J == 3:
                vitorias_time_J += 1
            elif vitorias_time_K == 3:
                vitorias_time_K += 1
            elif vitorias_time_L == 3:
                vitorias_time_L += 1
            elif vitorias_time_M == 3:
                vitorias_time_M += 1
            elif vitorias_time_N == 3:
                vitorias_time_N += 1
            elif vitorias_time_O == 3:
                vitorias_time_O += 1
            elif vitorias_time_P == 3:
                vitorias_time_P += 1
            
if vitorias_time_A == 4:
    print("Time A ganhou!")
elif vitorias_time_B == 4:
    print("Time B ganhou!")
elif vitorias_time_C == 4:
    print("Time C ganhou!")
elif vitorias_time_D == 4:
    print("Time D ganhou!")
elif vitorias_time_E == 4:
    print("Time E ganhou!")
elif vitorias_time_F == 4:
    print("Time F ganhou!")
elif vitorias_time_G == 4:
    print("Time G ganhou!")
elif vitorias_time_H == 4:
    print("Time H ganhou!")
elif vitorias_time_I == 4:
    print("Time I ganhou!")
elif vitorias_time_J == 4:
    print("Time J ganhou!")
elif vitorias_time_K == 4:
    print("Time K ganhou!")
elif vitorias_time_L == 4:
    print("Time L ganhou!")
elif vitorias_time_M == 4:
    print("Time M ganhou!")
elif vitorias_time_N == 4:
    print("Time N ganhou!")
elif vitorias_time_O == 4:
    print("Time O ganhou!")
elif vitorias_time_P == 4:
    print("Time P ganhou!")


