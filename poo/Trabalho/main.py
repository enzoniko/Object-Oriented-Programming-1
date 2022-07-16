from http.client import OK
from os import curdir, link
from re import S
from filme import Filme, filmes
from helpers import most_empty, lugares_disponiveis, lista_strings_para_string
from sessao import Sessao, sessoes
from sala import Sala, LINHAS, COLUNAS, salas


def main():
    # Loop pra saber se o usuario é adm ou não
    while True:

        # Pergunta pro usuário se ele é um administrador
        is_adm = input("Voce é administrador? (S/N) ").upper()

        # Se ele for pede confirmação por senha, e mostra o menu para administrador
        if is_adm == "S":
            print("Bem vindo administrador")
            break

        # Se ele não for administrador, mostra o menu para usuário
        elif is_adm == "N":
            # Printa a lista de filmes
            print()
            print("Lista de filmes disponíveis:")
            print()
            for filme in range(len(filmes)):
                print(f"{filme + 1}: ", end="")
                filmes[filme].print_info()
            print('-----------------------------------------------------')
            # Pergunta qual o número do filme que o usuário deseja
            while True:
                numero_do_filme = int(
                    input("Digite o número do filme que você deseja assistir: "))
                if (numero_do_filme - 1) in range(len(filmes)):
                    break
                else:
                    print("Opção Invalida")
            # Pega o nome do filme relacionado com o número digitado pelo usuário
            nome_do_filme = filmes[numero_do_filme - 1].get_nome()

            print(
                f"Sessões de {nome_do_filme.upper()}: ")
            print()
            # Pra cada sessão da lista de sessões
            for sessao in range(len(sessoes)):

                # Se o nome do filme da sessão for o mesmo do filme que o usuário deseja assistir
                if sessoes[sessao].get_nome() == nome_do_filme:

                    print(f"{sessao + 1}: ", end="")
                    # Mostra a sessão
                    sessoes[sessao].print_info()
                    print()

            # Pergunta qual a sessão que o usuário deseja assistir
            while True:
                numero_da_sessao = int(
                    input("Digite o número da sessão que você deseja assistir "))
                if (numero_da_sessao - 1) in range(len(sessoes)):
                    break
                else:
                    print("Opção Invalida")
            # Mostra a sessão escolhida
            # Mostra o nome
            print(sessoes[numero_da_sessao - 1].get_nome().upper(), end=' ')
            # Mostra se é legando ou não
            if sessoes[numero_da_sessao - 1].get_legenda() == True:
                print("LEGENDADO", end=' ')
            else:
                print("DUBLADO", end=' ')
            # Mostra se é 3D ou não
            if sessoes[numero_da_sessao - 1].get_DDD() == True:
                print("3D")
            else:
                print("2D")
            # Mostra os horários da sessão
            print("Horários: ")
            for horario in range(len(sessoes[numero_da_sessao - 1].get_horarios())):
                print(f"{horario + 1}: ", end="")
                print(sessoes[numero_da_sessao - 1].get_horarios()[horario])
            print()
            # Pergunta qual o horário que o usuário deseja assistir
            while True:
                numero_do_horario = int(
                    input("Digite o número do horário que você deseja assistir: "))
                # Se o horario não existir
                if (numero_do_horario - 1) in range(len(sessoes[numero_da_sessao - 1].get_horarios())):
                    break
                else:
                    print("Opção Invalida")
            print()
            # Pega o horário relacionado com o número digitado pelo usuário
            horario = sessoes[numero_da_sessao -
                              1].get_horarios()[numero_do_horario - 1]

            # Mostra a sessão escolhida
            # Mostra o nome
            print(sessoes[numero_da_sessao - 1].get_nome().upper(), end=' ')
            # Mostra se é legando ou não
            if sessoes[numero_da_sessao - 1].get_legenda() == True:
                print("LEGENDADO", end=' ')
            else:
                print("DUBLADO", end=' ')
            # Mostra se é 3D ou não
            if sessoes[numero_da_sessao - 1].get_DDD() == True:
                print("3D", end=' ')
            else:
                print("2D", end=' ')

            # Mostra o horário escolhido
            print(horario)
            print()

            # Pergunta quantos ingressos o usuário deseja comprar
            while True:
                quantidade_ingressos = int(input(
                    "Digite a quantidade total de ingressos que você deseja comprar dessa sessão: "))

                # Se a quantidade de ingressos pedidos for menor ou igual que a quantidade de poltronas disponíveis (Sala mais vazia que passa a sessão escolhida) e for maior que 0
                if quantidade_ingressos <= most_empty([[sala.get_poltronas() for sessao in sala.get_sessoes(
                ) if sessao == sessoes[numero_da_sessao - 1]] for sala in salas]) and quantidade_ingressos > 0:

                    # Pergunta quantos desses ingressos são meia entrada
                    while True:
                        # Verifica que a quantidade de meias não seja maior que a quantidade de ingressos pedidos
                        quantidade_meias = int(
                            input("Digite quantos ingressos do total são meia entrada: "))
                        if quantidade_meias <= quantidade_ingressos and quantidade_meias > 0:
                            break
                        else:
                            print(
                                "Quantidade de meias não pode ser maior que a quantidade de ingressos")
                    break
                else:
                    print("Não temos nenhuma sala com essa quantidade de poltronas!")

            # Printar as poltronas da sala mais vazia que passa a sessão escolhida para o usuário escolher as poltronas
            print("Poltronas: ")
            sala_mais_vazia = None
            for sala in salas:
                if lugares_disponiveis(sala.get_poltronas()) == most_empty([[sala.get_poltronas() for sessao in sala.get_sessoes(
                ) if sessao == sessoes[numero_da_sessao - 1]] for sala in salas]):
                    sala.printar_poltronas()
                    sala_mais_vazia = sala
                    break

            # Deixar o usuário escolher as poltronas
            poltronas_a_preencher = input(
                "Digite as coordenadas das poltronas que você deseja sentar separadas por um espaço: ").split()[:quantidade_ingressos]

            # Preencher a sala com as poltronas escolhidas pelo usuário
            erradas = sala_mais_vazia.preencher_poltronas(
                poltronas_a_preencher)

            # Se o usuário não escolher as poltronas corretamente
            while len(erradas) != 0:
                if len(erradas[0]) != 0 and len(erradas[1]) == 0:
                    letras_erradas = list(set(erradas[0]))
                    print(
                        f"Poltronas com letra(s) {lista_strings_para_string(letras_erradas)} não existem!")
                elif len(erradas[1]) != 0 and len(erradas[0]) == 0:
                    numeros_errados = list(set(erradas[1]))
                    print(
                        f"Poltronas com número(s) {lista_strings_para_string([str(num) for num in numeros_errados])} não existem!")
                elif len(erradas[0]) != 0 and len(erradas[1]) != 0:
                    letras_erradas = list(set(erradas[0]))
                    numeros_errados = list(set(erradas[1]))
                    print(
                        f"Poltronas com letra(s) {lista_strings_para_string(letras_erradas)} não existem!")

                    print(
                        f"Poltronas com número(s) {lista_strings_para_string([str(num) for num in numeros_errados])} não existem!")

                # Repetir o processo de escolha de poltronas até o usuário escolher as poltronas corretamente
                poltronas_a_preencher = input(
                    "Digite as coordenadas das poltronas que você deseja sentar separadas por um espaço: ").split()[:quantidade_ingressos]
                erradas = sala_mais_vazia.preencher_poltronas(
                    poltronas_a_preencher)

            # Printa a sala depois de preencher as poltronas
            sala.printar_poltronas()

            # ...Finalizar pagamento...

            break
        else:
            print("Opção Invalida")


if __name__ == '__main__':
    main()
