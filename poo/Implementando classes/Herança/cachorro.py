# Super classe Cachorro, possui raca, cor, peso, idade, nome_animal e nome_dono como atributos
class Cachorro:
    def __init__(self, raca, cor, peso, idade, nome_animal, nome_dono):
        self.raca = raca
        self.cor = cor
        self.peso = peso
        self.idade = idade
        self.nome_animal = nome_animal 
        self.nome_dono = nome_dono

# Modifica as informações da classe Cachorro
    def set_raca(self, raca):
        self.raca = raca
    def set_cor(self, cor):
        self.cor = cor
    def set_peso(self, peso):
        self.peso = peso
    def set_idade(self, idade):
        self.idade = idade
    def set_nome_animal(self, nome_animal):
        self.nome_animal = nome_animal
    def set_nome_dono(self, nome_dono):
        self.nome_dono = nome_dono

# Retorna as informações da classe Cachorro
    def get_raca(self):
        return self.raca
    def get_cor(self):
        return self.cor
    def get_peso(self):
        return self.peso
    def get_idade(self):
        return self.idade
    def get_nome_animal(self):
        return self.nome_animal
    def get_nome_dono(self):
        return self.nome_dono