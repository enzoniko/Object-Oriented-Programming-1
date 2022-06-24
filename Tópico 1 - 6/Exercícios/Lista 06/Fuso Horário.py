def hora_local_prevista(hora_saida, tempo_viagem, fuso_horario):
    hora_local = hora_saida + tempo_viagem + fuso_horario
    if hora_local >= 24:
        hora_local = hora_local % 24
    elif hora_local < 0:
        hora_local = 24 + hora_local
    print (hora_local)
    
    
hora_saida, tempo_viagem, fuso_horario = [int(value) for value in input("Digite o horário de saída, o tempo de viagem e o fuso horário do destino separados por um espaço: ").split()]
hora_local_prevista(hora_saida, tempo_viagem, fuso_horario)