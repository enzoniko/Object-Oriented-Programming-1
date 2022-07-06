class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.equilatero()
        self.isosceles()
        self.escaleno()
    
    def equilatero(self):
        if self.a == self.b and self.b == self.c:
            print("É um triângulo equilátero")
        else:
            print("Não é um triângulo equilátero")
    
    def isosceles(self):
        if self.a == self.b or self.b == self.c or self.a == self.c:
            print("É um triângulo isósceles")
        else:
            print("Não é um triângulo isósceles")
    
    def escaleno(self):
        if self.a != self.b and self.b != self.c and self.a != self.c:
            print("É um triângulo escaleno")
        else:
            print("Não é um triângulo escaleno")
        