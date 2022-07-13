from filme import Filme, filmes
from sessao import Sessao, sessoes


def main():

    # Pergunta pro usuário se ele é um administrador
    is_adm = input("Voce é administrador? (S/N) ").upper()

    # Se ele for pede confirmação por senha, e mostra o menu para administrador
    if is_adm == "S":
        print("Bem vindo administrador")

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
        numero_do_filme = int(
            input("Digite o número do filme que você deseja assistir: "))
        print()
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
        # CONTINUAR AQUI


if __name__ == '__main__':
    main()
