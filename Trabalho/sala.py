# Importa a classe Sessao do módulo sessao
from sessao import Sessao

# Importa a super classe Filme do módulo filme
from filme import Filme

# Cria a classe Sala que se associa com a classe Sessao


class Sala:

    # Construtor da classe Sala, recebe os atributos ocupada e cronograma (dicionário sessoes e seus horários associados)
    def __init__(self, ocupada=False, cronograma=dict()):
        self.cronograma = cronograma
        # Cria uma matriz de poltronas com 15 linhas e 20 colunas, inicialmente todas vazias
        self.poltronas = [[0]*20]*15
        self.ocupada = ocupada
        # Lista de sessões da sala
        self.sessoes = list()

    # REPENSAR
    def get_cronograma(self):
        return self.cronograma

    # get_poltronas retorna a matriz de poltronas
    def get_poltronas(self):
        return self.poltronas

    # get_ocupada retorna se a sala está ocupada ou não
    def get_ocupada(self):
        return self.ocupada

    # get_sessoes retorna a lista de sessões da sala
    def get_sessoes(self):
        return self.sessoes

    # REPENSAR
    def set_cronograma(self, cronograma):
        self.cronograma = cronograma

    # Função que prenche a matriz de poltronas dadas as poltronas a serem preenchidas
    def preencher_poltronas(self, poltronas):

        # Lista de letras para associar letra com número da poltrona
        letras = ["a", "b", "c", "d", "e", "f", "g",
                  "h", "i", "j", "k", "l", "m", "n", "o"]

        # Pra cada poltrona na lista de poltronas a serem preenchidas
        for poltrona in poltronas:
            # Cria uma cópia da linha da matriz de poltronas referente à letra da poltrona
            linha = self.poltronas[letras.index(poltrona[0])][:]
            # Preenche a coluna da linha da matriz de poltronas referente ao número da poltrona
            linha[int(poltrona[1:]) - 1] = 1
            # Atualiza a linha da matriz de poltronas referente à letra da poltrona
            self.poltronas[letras.index(poltrona[0])] = linha

    # set_ocupada define se a sala está ocupada ou não
    def set_ocupada(self, ocupada):
        self.ocupada = ocupada

    # print_info imprime informações da sala
    def print_info(self):
        print("Cronograma: ", self.cronograma)
        print("Poltronas: ", self.poltronas)
        print("Ocupada: ", self.ocupada)

    # Função que adiciona uma sessão à sala
    def add_sessao(self, sessao):

        # Cria um dicionário chamado cronograma
        cronograma = dict()
        # As chaves dos dicionários são os ids das sessões e os valores são os horários das sessões
        cronograma[sessao.id] = sessao.get_horarios()
        # Adiciona a sessão à lista de sessões da sala
        self.sessoes.append(sessao)
        # Atualiza o dicionário de cronograma
        self.cronograma.update(cronograma)

    # Função que remove uma sessão da sala
    def remove_sessao(self, sessao):

        # Variável para marcar se uma sessão foi removida
        removed = False
        # Para cada sessão na lista de sessões da sala
        for s in self.sessoes:
            # Se a sessão for a mesma que a sessão a ser removida
            if s == sessao:
                # Pra cada chave (id) do dicionário de cronograma
                for id in self.cronograma:
                    # Se o id da sessão for o mesmo do id da chave do dicionário de cronograma
                    if id == s.id:
                        # Remove essa chave do dicionário de cronograma
                        del self.cronograma[id]
                        break
                # Remove a sessão da lista de sessões da sala
                self.sessoes.remove(s)
                # Marca que a sessão foi removida
                removed = True
                break
        # Se a sessão não foi removida
        if removed == False:
            # Fala que a sessão não foi encontrada
            print("Sessão não encontrada")

    # Função que retorna uma lista de sessões que começam no horário dado
    def get_sessao(self, horario):

        # Variável para marcar se uma sessão foi encontrada
        encontrado = False
        # Pra cada chave(id) do dicionário de cronograma
        for id in self.cronograma:
            # Se o horário dado estiver na lista de horários que é o valor relacionado à chave do dicionário de cronograma
            if horario in self.cronograma[id]:
                # Pra cada sessão na lista de sessões da sala
                for sessao in self.sessoes:
                    # Se o id da sessão for o mesmo do id da chave do dicionário de cronograma
                    if id == sessao.id:
                        # Marca que a sessão foi encontrada
                        encontrado = True
                        # Retorna a sessão encontrada
                        return sessao
        # Se a sessão não foi encontrada
        if encontrado == False:
            # Retorna None
            return None


# Inicio Tests
s1 = Sessao("Titanic", ["Drama", "Romance"], ["2D", "3D"], [
            "Ingles", "Espanhol"], True, True, ["12:00", "17:00", "21:00"], "Ingles")
s2 = Sessao("Titanic", ["Drama", "Romance"], ["2D", "3D"], [
            "Ingles", "Espanhol"], False, True, ["9:00", "23:00"], "Espanhol")
sala1 = Sala()
sala1.add_sessao(s1)
sala1.add_sessao(s2)
sala1.get_sessoes()
print("REMOVED")
sala1.remove_sessao(s1)
sala1.get_sessoes()
sala1.get_sessao("9:00").print_info()
sala1.print_info()
print(len(sala1.get_poltronas()))
sala1.preencher_poltronas(["a1", "b2", "c3", "d4", "e5", "f6",
                           "g7", "h8", "i9", "j10", "k11", "l12", "m13", "n14", "o15"])
print(sala1.get_poltronas())
# Fim Tests
