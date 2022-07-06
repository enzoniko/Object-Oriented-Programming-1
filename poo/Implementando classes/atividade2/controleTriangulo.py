from triangulo import Triangulo

def verificar_triangulo(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        print("Não é um triângulo")
    elif a + b <= c or a + c <= b or b + c <= a:
        print("Não é um triângulo")
    else:
        triangulo = Triangulo(a, b, c)

while True:
    a, b, c = [int(x) for x in input("Digite os lados do triângulo separados por um espaço: ").split()][:3]
    verificar_triangulo(a, b, c)
    if input("Deseja continuar? (S/N): ").upper() == "N":
        print("Fim do programa")
        break
    print("-----------------------------------------------------")

