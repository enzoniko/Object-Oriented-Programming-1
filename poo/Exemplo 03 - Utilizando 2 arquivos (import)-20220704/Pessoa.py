#Exemplo 03 (usando 2 arquivos)

class Pessoa:
    
    def __init__(self,nome, idade, comendo=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        variavel_qualquer = "criando uma pessoa"
        print(variavel_qualquer, self.nome)
        
        
    def getNome(self):
        return self.nome
    
    def getIdade(self):
        return self.idade
    
    def setNome(self,nome):
        self.nome = nome
    
    def setIdade(self,idade):
        self.idade = idade