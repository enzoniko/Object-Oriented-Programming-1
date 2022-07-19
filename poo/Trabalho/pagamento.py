# PENSAR SE TEM ALGUMA OUTRA COISA PRA FAZER AQUI
class Pagamento():
    def __init__(self, ingressos, meias, forma="Dinheiro"):
        self.ingressos = ingressos
        self.meias = meias
        self.valor = 0
        self.set_valor(ingressos, meias)
        self.forma = forma

    def get_valor(self):
        return self.valor

    def get_forma(self):
        return self.forma

    def get_ingressos(self):
        return self.ingressos

    def get_meias(self):
        return self.meias

    def set_ingressos(self, ingressos):
        self.ingressos = ingressos

    def set_meias(self, meias):
        self.meias = meias

    def set_valor(self, ingressos, meias):
        self.valor = 30 * (ingressos - meias) + 15 * meias

    def set_forma(self, forma):
        self.forma = forma

    def print_info(self):
        print(f"Inteiras: {self.get_ingressos() - self.get_meias()}")
        print(f"Meias: {self.get_meias()}")
        print(f"Valor: R${self.get_valor()},00")
        print(f"Forma de pagamento: {self.get_forma()}")
