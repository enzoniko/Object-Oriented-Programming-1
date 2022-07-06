from cachorro import Cachorro

# Sub classe CachorroVip que herda de cachorro
class CachorroVip(Cachorro):

    # Possui restricao, banho e vantagem como atributos adicionais
    def __init__(self, restricao, banho, vantagem = False):
        super().__init__(raca, cor, peso, idade, nome_animal, nome_dono)
        self.restricao = restricao
        self.banho = banho
        self.vantagem = vantagem
    
    # Métodos que modificam cada atributo
    def set_restricao(self, restricao):
        self.restricao = restricao
    def set_banho(self, banho):
        self.banho = banho
    def set_vantagem(self, vantagem):
        self.vantagem = vantagem
    
    # Métodos que devolvem cada atributo
    def get_restricao(self):
        return self.restricao
    def get_banho(self):
        return self.banho
    def get_vantagem(self):
        return self.vantagem


