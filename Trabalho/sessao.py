# Importa a super classe Filme que vai ser herdada pela sub classe sessao
from filme import Filme

# Importa a função strings_list_to_string do módulo helpers que converte uma lista de strings em uma string separada por vírgula.
from helpers import strings_list_to_string

# Cria a sub classe Sessao que herda de FIlme


class Sessao(Filme):

    # Constructor da sub classe Sessao, recebe os atributos da super classe Filme e os atributos específicos de sessao (DDD, legenda, horarios, idioma)
    def __init__(self, nome, generos, dimensoes, idiomas, DDD, legendado, horarios, idioma):
        super().__init__(nome, generos, dimensoes, idiomas)
        self.DDD = DDD
        self.legendado = legendado
        self.horarios = horarios
        self.idioma = idioma
        self.id = id(self)

    # get_DDD retorna se a sessao é 3D ou não
    def get_DDD(self):
        return self.DDD

    # get_legenda retorna se a sessao é legendada ou não
    def get_legendado(self):
        return self.legendado

    # get_horarios retorna os horários da sessão
    def get_horarios(self):
        return self.horarios

    # get_idioma retorna o idioma da sessao
    def get_idioma(self):
        return self.idioma

    # set_DDD modifica se a sessao é 3D ou não
    def set_DDD(self, DDD):
        self.DDD = DDD

    # set_legenda modifica se a sessao é legendada ou não
    def set_legendado(self, legendado):
        self.legendado = legendado

    # set_horarios modifica os horários da sessão
    def set_horarios(self, horarios):
        self.horarios = horarios

    # set_idioma modifica o idioma da sessao
    def set_idioma(self, idioma):
        self.idioma = idioma

    # print_info imprime todos os atributos da sub classe Sessao
    def print_info(self):
        super().print_info()
        print(f"3D: {self.DDD}\nLegendado: {self.legendado}\nHorários: {strings_list_to_string(self.horarios)}\nIdioma: {self.idioma}")

    # modifica_info modifica todos os atributos da sub classe Sessao
    def modificar_info(self):
        super().modificar_info()
        self.DDD = input("3D: ")
        self.legendado = input("Legendado: ")
        self.horarios = input("Horários: ").split(", ")
        self.idioma = input("Idioma: ")

    # __eq__ compara se duas sessoes são iguais
    def __eq__(self, __o: object) -> bool:
        return super().__eq__(__o) and self.DDD == __o.DDD and self.legendado == __o.legendado and self.horarios == __o.horarios and self.idioma == __o.idioma
