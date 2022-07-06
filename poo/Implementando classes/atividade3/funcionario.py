class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumentarSalario(self):
        if self.salario >= 1500 and self.salario < 1750:
            return self.salario + (self.salario * 0.12)
        
        elif self.salario >= 1750 and self.salario < 2000:
            return self.salario + (self.salario * 0.10)
        
        elif self.salario >= 2000 and self.salario < 3000:
            return self.salario + (self.salario * 0.07)
        
        else:
            return self.salario + (self.salario * 0.05)

    def getInfo(self):
        return f"Nome: {self.nome}, Salário: {self.salario}, Salário Reajustado: {self.aumentarSalario()}"