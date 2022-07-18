alunos, computadores, queimados, sem_compilador = [int(x) for x in input().split()]
if computadores - (queimados + sem_compilador) < alunos:
    print("Igor Feliz!!")
elif queimados > sem_compilador:
    print("Caio, a culpa eh sua!!")
else:
    print("Igor bolado!!")
