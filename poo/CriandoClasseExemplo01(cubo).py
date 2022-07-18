class Cubo:
    '''classe para calcular o cubo de um número'''
    def __init__(self,valor):
        self.x = valor
        print("Objeto criado")
    
    def calcula_cubo(self):
        cubo = self.x + self.x + self.x
        return f"Cubo calculado: {str(cubo)}"

#main
print("oi")

#criando uma instância (objeto) da classe Cubo
teste = Cubo(10)

#como mostrar o conteúdo de um atributo
print("Valor de x: ",teste.x)

#fazendo a invocação de um método
c = teste.calcula_cubo()
print(c)