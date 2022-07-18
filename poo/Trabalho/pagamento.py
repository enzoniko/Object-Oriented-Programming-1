# PENSAR SE TEM ALGUMA OUTRA COISA PRA FAZER AQUI
class Pagamento():
    def __init__(self, ingressos, meias, forma):
        self.valor = self.set_valor(ingressos, meias)
        self.forma = forma

    def get_valor(self):
        return self.valor

    def get_forma(self):
        return self.forma

    def set_valor(self, ingressos, meias):
        self.valor = 30 * (ingressos - meias) + 15 * meias

    def set_forma(self, forma):
        self.forma = forma
