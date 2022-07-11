# Importa a função strings_list_to_string do módulo helpers que converte uma lista de strings em uma string separada por vírgula.
from helpers import strings_list_to_string

# Cria a classe Filme


class Filme:

    # Construtor da classe Filme, recebe os atributos do filme (nome, generos, dimensoes e idiomas)
    def __init__(self, nome, generos, dimensoes, idiomas):
        self.nome = nome
        self.generos = generos
        self.dimensoes = dimensoes
        self.idiomas = idiomas

    # get_nome retorna o nome do filme
    def get_nome(self):
        return self.nome

    # get_generos retorna os gêneros do filme
    def get_generos(self):
        return self.generos

    # get_dimensoes retorna as dimensões do filme
    def get_dimensoes(self):
        return self.dimensoes

    # get_idiomas retorna os idiomas do filme
    def get_idiomas(self):
        return self.idiomas

    # set_nome modifica o nome do filme
    def set_nome(self, nome):
        self.nome = nome

    # set_generos modifica os gêneros do filme
    def set_generos(self, generos):
        self.generos = generos

    # set_dimensoes modifica as dimensões do filme
    def set_dimensoes(self, dimensoes):
        self.dimensoes = dimensoes

    # set_idiomas modifica os idiomas do filme
    def set_idiomas(self, idiomas):
        self.idiomas = idiomas

    # print_info imprime as informações do filme
    def print_info(self):
        print(f"Nome: {self.nome}\nGêneros: {strings_list_to_string(self.generos)}\nDimensões: {strings_list_to_string(self.dimensoes)}\nIdiomas: {strings_list_to_string(self.idiomas)}")

    # modifica_info modifica as informações do filme
    def modificar_info(self):
        self.nome = input("Nome: ")
        self.generos = input("Gêneros: ").split(", ")
        self.dimensoes = input("Dimensões: ").split(", ")
        self.idiomas = input("Idiomas: ").split(", ")


# Inicio dos tests:
"""
f1 = Filme("Titanic", ["Drama", "Romance"], ["2D", "3D"], ["Ingles", "Espanhol"])
f2 = Filme("The Avengers", ["Ação", "Aventura"], ["2D", "3D"], ["Ingles", "Portugues"])

f1.print_info()
f2.modificar_info()
f2.print_info()
"""
# Fim dos tests
