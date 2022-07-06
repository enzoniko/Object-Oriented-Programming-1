# classe funcionário

class Funcionario:
    def __init__(self, idfuncionario, nome, cpf, sexo):
        self.idfuncionario = idfuncionario
        self.nome = nome
        self.cpf = cpf
        self.sexo = sexo
        
    def set_id(self, idfuncionario):
        self.idfuncionario = idfuncionario
    def set_nome(self, nome):
        self.nome = nome
    def set_cpf(self, cpf):
        self.cpf = cpf
    def set_sexo(self, sexo):
        self.sexo = sexo
    
    def get_id(self):
        return self.idfuncionario
    def get_nome(self):
        return self.nome
    def get_cpf(self):
        return self.cpf
    def get_sexo(self):
        return self.sexo
    
    