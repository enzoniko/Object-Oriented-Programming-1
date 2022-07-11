class FiguraGeometrica:
    def __init__(self, nome):
        self.nome = nome

    def area(self):
        return 0


class Quadrado(FiguraGeometrica):
    def __init__(self, nome, lado):
        super().__init__(nome)
        self.lado = lado

    def area(self):
        return self.lado * self.lado


class Triangulo(FiguraGeometrica):
    def __init__(self, nome, base, altura):
        super().__init__(nome)
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2


class Circulo(FiguraGeometrica):
    def __init__(self, nome, raio):
        super().__init__(nome)
        self.raio = raio

    def area(self):
        return 3.14 * (self.raio ** 2)
