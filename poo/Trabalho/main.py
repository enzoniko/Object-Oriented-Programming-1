from filme import Filme
from helpers import most_empty, lugares_disponiveis, lista_strings_para_string, verificador_input
from sessao import Sessao
from sala import Sala, LINHAS, COLUNAS, salas
from pagamento import Pagamento
# Função que preenche as poltronas de uma sala

# Lista de pagamentos (usar para mostrar o total faturado para o administrador)
pagamentos = []

sessoes = []
filmes = []
# DAR UM JEITO DE USAR O CRONOGRAMA DA SALA

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


def mostra_sessoes_de_cada_sala(printar_indice=False):
    for sala in range(len(salas)):
        print()
        print(f"Sala {sala + 1}:")
        print()
        if salas[sala].get_sessoes() == []:
            print("Nenhuma sessão cadastrada")
            print()
        for sessao in salas[sala].get_sessoes():
            for s in range(len(sessoes)):
                if sessoes[s].get_id() == sessao.get_id():
                    if printar_indice:
                        print(f"Opção {s + 1} : ")

                    mostrar_sessao(s + 1, mostrar_horarios=True)


def alterar_sessao(numero_da_sessao=None):
    if len(sessoes) == 0:
        print("Não existem sessões cadastradas")
        print()
        return
    if numero_da_sessao is None:

        mostra_sessoes_de_cada_sala(printar_indice=True)
        numero_da_sessao = verificador_input(
            "da sessão", sessoes, 'in', "Opção inválida!")

        # Mostra a sessão escolhida e seus horários
        mostrar_sessao(numero_da_sessao, mostrar_horarios=True)

    # Pergunta pelo nome do filme da sessão
    novo_nome = input(
        "Digite o nome do filme da sessão: ")
    # Pergunta pelo novo gênero da sessão
    novo_genero = input(
        "Digite o gênero da sessão: ").split()
    # Pergunta pelos novos horários da sessão
    novos_horarios = input(
        "Digite os horários da sessão: ").split()
    # Pergunta se a sessão é 3D ou não
    novo_DDD = input("É 3D? (S/N) ").upper() != 'N'
    # Pergunta se a sessão é legendada ou não

    novo_legenda = input("É legendada? (S/N) ").upper() != 'N'
    # Modifica as informações da sessão
    sessoes[numero_da_sessao - 1].modifica_info(
        novo_nome, novo_genero, novos_horarios, novo_DDD, novo_legenda)
    # Mostra a sessão escolhida e seus horários
    mostrar_sessao(numero_da_sessao, mostrar_horarios=True)


def excluir_sessao():
    mostra_sessoes_de_cada_sala(printar_indice=True)
    numero_da_sessao = verificador_input(
        "da sessão (para excluir)", sessoes, 'in', "Opção inválida!")

    # Mostra a sessão escolhida e seus horários
    mostrar_sessao(numero_da_sessao, mostrar_horarios=True)
    # Pergunta se o usuário deseja excluir a sessão
    if input("Deseja excluir a sessão? (S/N) ").upper() == 'S':
        for sala in salas:
            sala.remover_sessao(sessoes[numero_da_sessao - 1])
        sessoes.pop(numero_da_sessao - 1)
    else:
        return


def adicionar_sessao():
    sessoes.append(Sessao())
    alterar_sessao(len(sessoes))
    numero_da_sala = verificador_input(
        "da sala (pra por a sessão)", salas, 'in', "Opção inválida!")
    salas[numero_da_sala - 1].adicionar_sessao(sessoes[-1])
    filmes.append(Filme(sessoes[-1].get_nome(), sessoes[-1].get_generos()))


def main():
    # Loop pra saber se o usuario é adm ou não

    # Pergunta pro usuário se ele é um administrador
    is_adm = input("Voce é administrador? (S/N) ").upper()
    senha = ""
    while True:

        # Se ele for pede confirmação por senha, e mostra o menu para administrador
        if is_adm == "S":

            # Pergunta por senha
            if senha != "admin":
                senha = input("Digite a senha: (0 para sair) ")
            # Se a senha for correta, mostra o menu para o administrador
            while senha not in ["admin", "0"]:
                print("Senha incorreta!")
                senha = input("Digite a senha: (0 para sair) ")
            if senha == "admin":
                print()
                print("Menu: ")
                print("1: Consultar sessões")
                print("2: Alterar sessão")
                print("3: Adicionar sessão")
                print("4: Excluir sessão")
                print("5: Consultar fatura atual")
                print("6: Sair")

                op = verificador_input("da opção", list(
                    range(7)), 'in', "Opção inválida!")

                if op == 1:
                    mostra_sessoes_de_cada_sala()
                elif op == 2:
                    alterar_sessao()
                elif op == 3:
                    adicionar_sessao()
                elif op == 4:
                    excluir_sessao()
                elif op == 5:
                    if pagamentos == []:
                        print("Não existem pagamentos cadastrados")
                        print()
                    else:
                        total = sum(pagamento.get_valor()
                                    for pagamento in pagamentos)

                        print(f"Total faturado: R$ {total:.2f}")
                elif op == 6:
                    is_adm = input("Voce é administrador? (S/N) ").upper()
            if senha == "0":
                is_adm = input("Voce é administrador? (S/N) ").upper()

        elif is_adm == "N":
            while True:
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
                numero_da_sessao = sessoes.index(
                    [sessao for sessao in sessoes if sessao.get_nome() == nome_do_filme][numero_da_sessao - 1])
                # Mostra a sessão escolhida e seus horários
                mostrar_sessao(numero_da_sessao, mostrar_horarios=True)
                # CORRIGIR ERRO NA ESCOLHA DA SESSAO
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
                    cancelar = input(
                        "Deseja cancelar a compra? (S/N) ").upper()

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

                print("1: Comprar novos ingressos\n2: Sair ")
                encerrar = verificador_input("da opção (Comprar ou Sair)", [
                                             0, 0], 'in', 'Opção inválida')
                if encerrar == 1:
                    continue
                elif encerrar == 2:
                    is_adm = input("Você é administrador? (S/N) ").upper()
                    # DAR UM JEITO DE PEDIR A SENHA DENOVO
                    break
        else:
            is_adm = input("Você é administrador? (S/N) ").upper()


# Chama a função main no início do programa
if __name__ == '__main__':
    main()
