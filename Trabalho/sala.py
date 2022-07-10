from sessao import Sessao
from filme import Filme

class Sala:
    def __init__(self, ocupada = False, cronograma = dict()):
        self.cronograma = cronograma
        self.poltronas = [[]*20]*15
        self.ocupada = ocupada
        self.sessoes = list()

    def get_cronograma(self):
        return self.cronograma
    
    def get_poltronas(self):
        return self.poltronas
    
    def get_ocupada(self):
        return self.ocupada
    
    def get_sessoes(self):
        return self.sessoes
    
    def set_cronograma(self, cronograma):
        self.cronograma = cronograma
    
    def set_poltronas(self, poltronas):
        self.poltronas = poltronas
    
    def set_ocupada(self, ocupada):
        self.ocupada = ocupada
    
    def print_info(self):
        print("Cronograma: ", self.cronograma)
        print("Poltronas: ", self.poltronas)
        print("Ocupada: ", self.ocupada)

    def add_sessao(self, sessao):
        cronograma = dict()
        cronograma[sessao.id] = sessao.get_horarios()
        self.sessoes.append(sessao)
        self.cronograma.update(cronograma)

    def remove_sessao(self, sessao):
        removed = False
        for s in self.sessoes:
            if s == sessao:
                for id in self.cronograma:
                    if id == s.id:
                        del self.cronograma[id]
                        break
                self.sessoes.remove(s)
                removed = True
                break
        if removed == False:
            print("Sessão não encontrada")
        
    def get_sessao(self, horario):
        encontrado = False
        for id in self.cronograma:
            if horario in self.cronograma[id]:
                for sessao in self.sessoes:
                    if id == sessao.id:
                        encontrado = True
                        return sessao
        if encontrado == False:
            return None
    


# Inicio Tests
s1 = Sessao("Titanic", ["Drama", "Romance"], ["2D", "3D"], ["Ingles", "Espanhol"], True, True, ["12:00", "17:00", "21:00"], "Ingles")
s2 = Sessao("Titanic", ["Drama", "Romance"], ["2D", "3D"], ["Ingles", "Espanhol"], False, True, ["9:00", "23:00"], "Espanhol")
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
# Fim Tests