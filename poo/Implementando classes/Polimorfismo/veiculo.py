class Veiculo:
    def __init__(self, cor, marca, modelo, qtd_tanque):
        self.cor = cor
        self.marca = marca
        self.modelo = modelo
        self.qtd_tanque = qtd_tanque
        self.limit = 100

    def get_cor(self):
        return self.cor

    def get_marca(self):
        return self.marca

    def get_modelo(self):
        return self.modelo

    def get_qtd_tanque(self):
        return self.qtd_tanque

    def set_cor(self, cor):
        self.cor = cor

    def set_marca(self, marca):
        self.marca = marca

    def set_modelo(self, modelo):
        self.modelo = modelo

    def set_qtd_tanque(self, qtd_tanque):
        self.qtd_tanque = qtd_tanque

    def set_limit(self, limit):
        self.limit = limit

    def abastecer(self, litros):
        print(f"Tentando abastecer {litros} litros")
        if litros + self.qtd_tanque > self.limit:
            print("Capacidade máxima atingida, foi possível abastecer: ",
                  self.limit - self.qtd_tanque)
            self.qtd_tanque = self.limit

        else:
            self.qtd_tanque += litros

    def imprime(self):
        print(
            f"O veículo é {self.get_cor()} {self.get_marca()} {self.get_modelo()} tem {self.get_qtd_tanque()} litros")
