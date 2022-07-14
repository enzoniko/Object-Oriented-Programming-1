# Importa a sub classe Sessao do módulo sessao
from sessao import Sessao, sessoes

# Importa a função printa_matriz e check_1 do módulo helpers
from helpers import check_1, printa_matriz

# Constantes de colunas e linhas da matriz de poltronas
COLUNAS = 10
LINHAS = 15
# Cria a classe Sala que se associa com a classe Sessao


class Sala:

    # Construtor da classe Sala, recebe os atributos da classe Sala (ocupada, cronograma(dicionário de sessões e seus horários associados))
    def __init__(self, ocupada=False, cronograma=dict()):
        self.cronograma = cronograma
        # Cria uma matriz de poltronas com 15 linhas e 20 colunas, incialmente todas as poltronas estão livres
        self.poltronas = [[0] * COLUNAS]*LINHAS
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
        # Lista de letras para associar letra com número da poltrona
        letras = ["a", "b", "c", "d", "e", "f", "g",
                  "h", "i", "j", "k", "l", "m", "n", "o"]

        # Printa a numeração das colunas
        print(" ", end=" ")
        for coluna in range(len(self.poltronas[0]) - 1, 0, -1):
            if coluna <= 9:
                print(f"  {coluna}  ", end=" ")
            else:
                print(f"  {coluna} ", end=" ")

        # Printa a letra da linha seguida por cada poltrona da linha
        for linha in range(len(self.poltronas) - 1, 0, -1):
            print()
            print(letras[linha - 1], end=" ")
            for coluna in range(len(self.poltronas[0]) - 1, 0, -1):
                # Bota um x na poltrona se ela estiver ocupada
                print(f"[ {check_1(self.poltronas[linha][coluna])} ]", end=" ")

        # Printa a posição da TELA
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
        print(f"Poltronas:")
        printa_matriz(self.poltronas)
        print(f"Sessões: {self.sessoes}")

    # Função que adiciona uma sessão à sala (cronograma)
    def adicionar_sessao(self, sessao):
        chave = sessao.get_id()
        valor = sessao.get_horarios()
        # Atualiza o cronograma com a sessão
        self.cronograma[chave] = valor

        # Adiciona a sessão à lista de sessões
        self.sessoes.append(sessao)
    # Função que remove sessão da sala (cronograma)
    # Função que devolve a sessão que passara em um determinado horário

    def get_sessao_from_cronograma(self):
        for id in self.cronograma:
            for sessao in self.sessoes:
                if sessao.get_id() == id:
                    sessao.print_info()


# Exemplo de lista de salas
sala1 = Sala()
sala1.preencher_poltronas(["a1", "b2", "c3", "d4", "e5", "f6", "a7",
                          "h8", "a9", "f10"])
sala1.adicionar_sessao(sessoes[0])
sala1.adicionar_sessao(sessoes[3])

sala2 = Sala()
sala2.preencher_poltronas(["e5", "f6", "a7", "h8", "a9", "f10"])
sala2.adicionar_sessao(sessoes[1])
sala2.adicionar_sessao(sessoes[2])

salas = [sala1, sala2]
'''
# Inicio testes
sala1 = Sala()
sala1.preencher_poltronas(["a1", "b2", "c3", "d4", "e5", "f6", "a7",
                          "h8", "a9", "f10"])
sala1.printar_poltronas()

s1 = Sessao("Titanic", ["drama", "romance"], ["19:00", "20:00"], True, True)
s2 = Sessao("The Godfather", ["drama", "crime"],
            ["14:00", "23:00"], True, True)
sala1.adicionar_sessao(s1)
sala1.adicionar_sessao(s2)
sala1.get_sessao_from_cronograma()

# Fim testes
'''
