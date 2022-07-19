from filme import Filme, filmes
from helpers import most_empty, lugares_disponiveis, lista_strings_para_string, verificador_input
from sessao import Sessao, sessoes
from sala import Sala, LINHAS, COLUNAS, salas
from pagamento import Pagamento
# Função que preenche as poltronas de uma sala

# Lista de pagamentos (usar para mostrar o total faturado para o administrador)
pagamentos = []

# Função que preenche as poltronas de uma sala


def preencher_poltronas(sala_mais_vazia, quantidade_ingressos):
    # Deixar o usuário escolher as poltronas
    poltronas_a_preencher = input(
        "Digite as coordenadas das poltronas que você deseja sentar separadas por um espaço: ").split()[:quantidade_ingressos]

    # Preencher a sala com as poltronas escolhidas pelo usuário
    erradas = sala_mais_vazia.preencher_poltronas(
        poltronas_a_preencher)

    # Se o usuário não escolher as poltronas corretamente
    while erradas != []:
        letras_erradas = list(set(erradas[0]))
        numeros_errados = list(set(erradas[1]))
        if erradas[2] != []:
            print(
                f"Poltrona(s) {lista_strings_para_string(list(set(erradas[2])))} já estão ocupadas!")
        if erradas[0] != [] and erradas[1] == []:
            print(
                f"Poltronas com letra(s) {lista_strings_para_string(letras_erradas)} não existem!")
        elif erradas[1] != [] and erradas[0] == []:
            print(
                f"Poltronas com número(s) {lista_strings_para_string([str(num) for num in numeros_errados])} não existem!")
        elif erradas[0] != [] and erradas[1] != []:
            print(
                f"Poltronas com letra(s) {lista_strings_para_string(letras_erradas)} não existem!")

            print(
                f"Poltronas com número(s) {lista_strings_para_string([str(num) for num in numeros_errados])} não existem!")

        # Repetir o processo de escolha de poltronas até o usuário escolher as poltronas corretamente
        poltronas_a_preencher = input(
            "Digite as coordenadas das poltronas que você deseja sentar separadas por um espaço: ").split()[:quantidade_ingressos]
        erradas = sala_mais_vazia.preencher_poltronas(
            poltronas_a_preencher)

    # Retornar a lista de poltronas que o usuário escolheu
    return poltronas_a_preencher

# Função que mostra os filmes disponíveis


def printar_filmes():
    # Printa a lista de filmes
    print()
    print("Lista de filmes disponíveis:")
    print()
    for filme in range(len(filmes)):
        print(f"{filme + 1}: ", end="")
        filmes[filme].print_info()
        print()
    print('-----------------------------------------------------')

# Função que printa as sessões de um filme


def printar_sessoes(nome_do_filme):
    print()
    print(f"Sessões de {nome_do_filme.upper()}: ")
    print()
    # Pra cada sessão da lista de sessões cujo nome do filme é o mesmo que o usuário deseja assistir
    for sessao in range(len([sessao for sessao in sessoes if sessao.get_nome() == nome_do_filme])):
        print(f"{sessao + 1}: ", end="")
        # Mostra a sessão
        sessoes[sessao].print_info()
        print()
    print('-----------------------------------------------------')

# Função que mostra a sessão escolhida e opcionalmente seus horários


def mostrar_sessao(numero_da_sessao, mostrar_horarios=False):
    print()
    # Mostra a sessão
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

    if mostrar_horarios:
        print()
        # Mostra os horários da sessão
        print("Horários: ")
        print()
        for horario in range(len(sessoes[numero_da_sessao - 1].get_horarios())):
            print(f"{horario + 1}: ", end="")
            print(sessoes[numero_da_sessao - 1].get_horarios()[horario])
            print()
        print('-----------------------------------------------------')

# Função que retorna a sala mais vazia dado a quantidade de lugares disponíveis na sala mais vazia e a sessão escolhida


def sala_mais_vazia(quantidade_lugares_disponiveis_sala_mais_vazia, sessao):
    # Printar as poltronas da sala mais vazia que passa a sessão escolhida para o usuário escolher as poltronas
    print("Poltronas: ")
    for sala in salas:
        if sessao in sala.get_sessoes() and lugares_disponiveis(sala.get_poltronas()) == quantidade_lugares_disponiveis_sala_mais_vazia:
            sala.printar_poltronas()
            return sala

# Função que printa o comprovante de compra


def comprovante(numero_da_sessao, horario, poltronas, pagamento):
    print()
    print("Comprovante de compra: ")
    # Mostra a sessão
    mostrar_sessao(numero_da_sessao)
    # Mostra o horário
    print(horario)
    # Mostra as poltronas
    print(f"Poltronas escolhidas: {lista_strings_para_string(poltronas)}")
    # Mostra o pagamento
    pagamento.print_info()
    print("-----------------------------------------------------")
# Função principal do programa


def main():
    # Loop pra saber se o usuario é adm ou não
    while True:

        # Pergunta pro usuário se ele é um administrador
        is_adm = input("Voce é administrador? (S/N) ").upper()

        # Se ele for pede confirmação por senha, e mostra o menu para administrador
        if is_adm == "S":
            # FAZER AS FUNÇÕES DE ADMINISTRADOR
            break

        # Se ele não for administrador, mostra o menu para usuário
        elif is_adm == "N":
            # Printa a lista de filmes
            printar_filmes()

            # Pergunta qual o número do filme que o usuário deseja
            numero_do_filme = verificador_input(
                "do filme", filmes, "in", "Opção inválida")

            # Pega o nome do filme relacionado com o número digitado pelo usuário
            nome_do_filme = filmes[numero_do_filme - 1].get_nome()

            # Printa a lista de sessões do filme
            printar_sessoes(nome_do_filme)

            # Pergunta qual a sessão que o usuário deseja assistir
            numero_da_sessao = verificador_input(
                "da sessão", [sessao for sessao in sessoes if sessao.get_nome() == nome_do_filme], "in", "Opção inválida")

            # Mostra a sessão escolhida e seus horários
            mostrar_sessao(numero_da_sessao, mostrar_horarios=True)

            # Pergunta qual o horário que o usuário deseja assistir
            numero_do_horario = verificador_input(
                "do horário", sessoes[numero_da_sessao - 1].get_horarios(), "in", "Opção inválida")

            # Pega o horário relacionado com o número digitado pelo usuário
            horario = sessoes[numero_da_sessao -
                              1].get_horarios()[numero_do_horario - 1]

            # Mostra a sessão escolhida
            mostrar_sessao(numero_da_sessao)

            # Mostra o horário escolhido
            print(horario)
            print()

            # Quantidade de lugares disponíveis na sala mais vazia que passa a sessão escolhida
            quantidade_lugares_disponiveis_sala_mais_vazia = most_empty([[sala.get_poltronas() for sessao in sala.get_sessoes(
            ) if sessao == sessoes[numero_da_sessao - 1]] for sala in salas])

            # Pergunta quantos ingressos o usuário deseja comprar
            quantidade_ingressos = verificador_input("de ingressos", [
                                                     quantidade_lugares_disponiveis_sala_mais_vazia], "<=", "Não temos nenhuma sala com essa quantidade de poltronas!")

            # Pergunta quantos desses ingressos são meia entrada
            quantidade_meias = verificador_input("de meias entradas", [
                                                 quantidade_ingressos], "<=", "Quantidade de meias não pode ser maior que a quantidade de ingressos")

            # Printar as poltronas da sala mais vazia que passa a sessão escolhida para o usuário escolher as poltronas
            sala = sala_mais_vazia(
                quantidade_lugares_disponiveis_sala_mais_vazia, sessoes[numero_da_sessao - 1])

            # Preenche as poltronas da sala mais vazia com as poltronas escolhidas pelo usuário
            poltronas_escolhidas = preencher_poltronas(
                sala, quantidade_ingressos)

            # Printa a sala depois de preencher as poltronas
            sala.printar_poltronas()
            print("-----------------------------------------------------")

            # FINALIZAR PAGAMENTO
            # Inicia o pagamento
            pagamento = Pagamento(quantidade_ingressos, quantidade_meias)
            # Mostrar o preço total
            print(f"Preço total: R$ {pagamento.get_valor()}")
            # Pergunta se o usuário deseja pagar com crédito, dinheiro ou débito
            print("Forma de pagamento:\n1 - Crédito\n2 - Débito\n3 - Dinheiro")
            # Formas de pagamento
            formas = ["Crédito", "Débito", "Dinheiro"]
            # Pega a forma que o usuário deseja pagar
            forma = verificador_input(
                "da forma de pagamento", formas, "in", "Opção inválida")
            # Modificia a forma de pagamento do pagamento
            pagamento.set_forma(formas[forma - 1])

            while True:
                # Pergunta pro usuário se ele deseja confirmar a compra
                confirmar = input("Confirmar compra? (S/N) ").upper()

                # Se ele confirmar, mostra o pagamento
                if confirmar == "S":
                    # Pagamento realizado com sucesso!
                    print("Pagamento realizado com sucesso!")

                    # Comprovante do pagamento
                    comprovante(numero_da_sessao, horario,
                                poltronas_escolhidas, pagamento)

                    # Adiciona o pagamento na lista de pagamentos
                    pagamentos.append(pagamento)
                    break

                # Se ele não confirmar, pergunta se ele quer cancelar a compra
                cancelar = input("Deseja cancelar a compra? (S/N) ").upper()

                # Se ele quer cancelar
                if cancelar == "S":
                    # Cancela o pagamento
                    print("Compra cancelada!")
                    # Esvazia as poltronas escolhidas pelo usuário
                    sala.esvaziar_poltronas(poltronas_escolhidas)
                    # Printa a sala depois de esvaziar as poltronas
                    sala.printar_poltronas()
                    print("-----------------------------------------------------")
                    break

            break
        else:
            print("Opção Invalida")


# Chama a função main no início do programa
if __name__ == '__main__':
    main()
