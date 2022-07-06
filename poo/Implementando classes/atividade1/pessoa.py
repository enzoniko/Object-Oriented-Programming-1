class Pessoa:
    def __init__(self, nome, idade, comendo = False, falando = False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
    
    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo!')
        else:
            print(f'{self.nome} está comendo {alimento}')
            self.comendo = True
    
    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo')
        self.comendo = False
    
    def falar(self, frase):
        if self.falando:
            print(f'{self.nome} já está falando!')
        else:
            print(f'{self.nome} está falando: {frase}')
            self.falando = True
    
    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando')
        self.falando = False
    
    def imprime_dados(self):
        print(f"{self.nome} tem {self.idade} anos. \nEstá comendo: {self.comendo} \nEstá falando: {self.falando}")
    
