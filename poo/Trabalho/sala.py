# Importa a sub classe Sessao do módulo sessao
from sessao import Sessao

# Importa a função printa_matriz e check_1 do módulo helpers
from helpers import check_1, printa_matriz

# Cria a classe Sala que se associa com a classe Sessao


class Sala:

    # Construtor da classe Sala, recebe os atributos da classe Sala (ocupada, cronograma(dicionário de sessões e seus horários associados))
    def __init__(self, ocupada=False, cronograma=dict()):
        self.cronograma = cronograma
        # Cria uma matriz de poltronas com 15 linhas e 20 colunas, incialmente todas as poltronas estão livres
        self.poltronas = [[0] * 10]*15
        self.ocupada = ocupada
        # Lista de sessões da sala
        self.sessoes = list()

    # getters e setters:

    def get_cronograma(self):
        return self.cronograma

    # get_poltronas retorna a matriz de poltronas
    def get_poltronas(self):
        return self.poltronas

    # get_ocupada retorna se a sala está ocupada
    def get_ocupada(self):
        return self.ocupada

    # get_sessoes retorna a lista de sessões da sala
    def get_sessoes(self):
        return self.sessoes

    def set_cronograma(self, cronograma):
        self.cronograma = cronograma

    # Método que preenche a matriz de poltronas com as poltronas a serem preenchidas
    def preencher_poltronas(self, poltronas):
        # Lista de letras para associar letra com número da poltrona
        letras = ["a", "b", "c", "d", "e", "f", "g",
                  "h", "i", "j", "k", "l", "m", "n", "o"]

        # Pra cada poltronas na lista de poltronas a serem preenchidas
        for poltrona in poltronas:
            # Pega a letra da poltrona
            letra = poltrona[0]
            # Pega o número da poltrona
            numero = int(poltrona[1:]) - 1
            # Pega o índice da letra na lista de letras
            indice = letras.index(letra)
            # Faz uma cópia da linha de índice "incide" da matriz de poltronas
            linha = self.poltronas[indice][:]
            # Substitui o número da poltrona pelo valor 1
            linha[numero] = 1
            # Atualiza a linha na matriz de poltronas
            self.poltronas[indice] = linha

    def printar_poltronas(self):
        letras = ["a", "b", "c", "d", "e", "f", "g",
                  "h", "i", "j", "k", "l", "m", "n", "o"]

        print(" ", end=" ")
        for coluna in range(len(self.poltronas[0]) - 1, 0, -1):
            if coluna <= 9:
                print(f"  {coluna}  ", end=" ")
            else:
                print(f"  {coluna} ", end=" ")

        for linha in range(len(self.poltronas) - 1, 0, -1):
            print()
            print(letras[linha - 1], end=" ")
            for coluna in range(len(self.poltronas[0]) - 1, 0, -1):
                print(f"[ {check_1(self.poltronas[linha][coluna])} ]", end=" ")

        print()
        t = "TELA"
        print(t.center((int(len(self.poltronas[0])*6)) - 4))

    # set_ocupada modifica se a sala está ocupada

    def set_ocupada(self, ocupada):
        self.ocupada = ocupada

    # print_info imprime os informações da sala
    def print_info(self):
        print(f"Ocupada: {self.ocupada}")
        print(f"Cronograma: {self.cronograma}")
        print(f"Poltronas: \n{printa_matriz(self.poltronas)}")
        print(f"Sessões: {self.sessoes}")

    # Função que adiciona uma sessão à sala (cronograma)
    # Função que remove função da sala (cronograma)
    # Função que devolve a sessão que que passara em um determinado horário


sala1 = Sala()
sala1.preencher_poltronas(["a1", "b2", "c3", "d4", "e5", "f6", "a7",
                          "h8", "a9", "f10"])
sala1.printar_poltronas()
