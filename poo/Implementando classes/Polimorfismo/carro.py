from veiculo import Veiculo


class Carro(Veiculo):
    def __init__(self, cor, marca, modelo, qtd_tanque, ano):
        super().__init__(cor, marca, modelo, qtd_tanque)
        self.ano = ano
        self.limit = 50

    def get_ano(self):
        return self.ano

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
            f"O veículo é {self.get_cor()} {self.get_marca()} {self.get_modelo()} de {self.get_ano()} tem {self.get_qtd_tanque()} litros")
