#usando métodos acessores para ler e alterar o conteúdo de um atributo

class Pessoa:
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade
    
    def getNome(self):
        return self.nome
    
    def getIdade(self):
        return self.idade
    
    def setNome(self,nome):
        self.nome = nome
    
    def setIdade(self,idade):
        self.idade = idade
        
        
#main
nome = input("Digite um nome: ")
idade = int(input("Digite a idade: "))
p1 = Pessoa(nome, idade)

#print(p1)
print(p1.nome)
print(p1.idade)
# ou
print(p1.getNome())
print(p1.getIdade())

#exemplo do uso do set
nome = input("Digite um nome: ")
idade = int(input("Digite a idade: "))
p2 = Pessoa(nome, idade)
print(p2.getNome())

# quando quer alterar o valor do atributo, passa o novo valor por parâmetro
#ou p2.setNome("Maria")
p2.setNome(input("Digite o novo nome:"))
print("Nome atualizado: ",p2.getNome())