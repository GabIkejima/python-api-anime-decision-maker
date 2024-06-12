"""""
@autor
Gabriel Higa Ikejima
@version
1.1
@since
12 / 06 / 2024
"""

import os
import sys


from interface import *
from utils import *
from request import *
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# Lista de animes, para adicionar manualmente [ainda em versão beta, pode ocorrer alguns erros ao exibir detalhes] é necessário digitar o nome do anime:
# COMPLETO(evitar usar siglas) / ENTRE ASPAS SIMPLES / INTEIRAMENTE MINÚSCULO / SEPARADO POR ESPAÇOS / PRIORIZAR O TÍTULO JAPONES

anime_list = ['naruto', 'haikyuu', 'one piece', 'dragon ball', 'a viagem de chihiro', 'castelo animado', 'Hauru no Ugoku Shiro', 'akira']
anime_list = list(filter(None, anime_list))

# -------------------------------------------------------------------
# MENU PRINCIPAL
# -------------------------------------------------------------------

def menu_inicial():
    cls()
    # Para adicionar, remover ou alterar alguma opção do menu, basta alterar a seguinte lista:
    lista_de_opcoes_menu = ['Escolha animes por mim', 'Sugerir animes por mood - em desenvolvimento', 'Ver minha lista de animes', 'Editar minha lista de animes', 'Sair']

    printar_titulo("Olá, sou o ajudante de decisões v.01")
    printar_opcoes(lista_de_opcoes_menu)
    numero_opcao_escolhida_menu = validar_opcao("Digite o número da sua opção --> ", len(lista_de_opcoes_menu))

    # Direciona o usuário conforme a opção escolhida
    match numero_opcao_escolhida_menu:
        case 1:
            menu_animes()
        case 2:
            sugerir_anime_por_mood()
            menu_inicial()
        case 3:
            printar_lista_de_animes(anime_list)
            input('Aperte enter para continuar --> ')
            menu_inicial()
        case 4:
            editar_lista_de_animes(anime_list)
        case 5:
            printar_titulo('Até a próxima! ;)')
        case _:
            menu_inicial()

# -------------------------------------------------------------------
# MENU SECUNDÁRIO - "Escolha animes por mim"
# -------------------------------------------------------------------

# Opção 1 do menu principal, para gerar um anime aleatório
def menu_animes():
    cls()
    # Para adicionar, remover ou alterar alguma opção do menu de anime, basta alterar o seguinte dicionário:
    lista_de_opcoes_anime = ['Gerar outros animes', 'Exibir detalhes dos animes', 'Voltar', 'Sair']
    numero_opcao_escolhida_anime = 1
    while (numero_opcao_escolhida_anime == 1):
        anime_gerado_da_lista = gerar_anime_aleatorio_da_lista(anime_list) # gera um anime aleatorio da lista de animes
        anime_gerado_da_api = gerar_informacao_do_anime_por_ID(random.randint(0, 500)) # gera um anime aleatorio da API

        printar_linha()
        printar_anime(anime_gerado_da_lista, 'Sugestão de anime da sua lista: ')
        printar_anime(anime_gerado_da_api['titulo'], 'Sugestão de anime da API: ')
        printar_linha()

        printar_opcoes(lista_de_opcoes_anime)
        numero_opcao_escolhida_anime = validar_opcao("Digite o número da sua opção --> ", len(lista_de_opcoes_anime))

        match numero_opcao_escolhida_anime:
            case 1:
                continue

            # Exibir detalhes dos animes
            case 2:
                lista_de_opcoes_detalhes = [anime_gerado_da_lista, anime_gerado_da_api['titulo'], 'Ambos']

                printar_titulo('Exibir detalhes de qual anime?')
                printar_opcoes(lista_de_opcoes_detalhes)
                numero_opcao_escolhida_detalhes = validar_opcao("Digite o número da sua opção --> ", len(lista_de_opcoes_detalhes))

                # Chamada da função do menu exibir detalhes
                menu_exibir_detalhes_dos_animes(numero_opcao_escolhida_detalhes, anime_gerado_da_lista, anime_gerado_da_api)

                input('Aperte enter para continuar --> ')
                menu_inicial()
                break

            case 3:
                menu_inicial()
                break
            case 4:
                printar_titulo('Até a próxima! ;)')
                break
            case _:
                menu_animes()
                break

# -------------------------------------------------------------------
# MENU SECUNDÁRIO - "Sugerir anime por mood"
# -------------------------------------------------------------------

def sugerir_anime_por_mood():
    cls()
    printar_titulo('Vou sugerir um anime com base no seu mood!')
    print('Recurso em construção!')


# -------------------------------------------------------------------
# MENU SECUNDÁRIO - "Ver minha lista de animes"
# -------------------------------------------------------------------

# Opção 3 do menu principal, para mostrar os items da lista de animes
def printar_lista_de_animes(lista_de_animes):
    try:
        # Verifica se a lista de animes está vazia
        if not lista_de_animes:
            printar_entre_linhas('Sua lista de anime está vazia!')
        else:
            printar_linha()
            print('Sua lista de animes contém os seguintes animes: ')
            printar_opcoes(lista_de_animes, '*')
            printar_linha()
    except Exception:
        printar_entre_linhas('Erro ao verificar a lista de animes!')

# Opção 4 do menu principal, para editar a lista de animes
def editar_lista_de_animes(anime_list):
    cls()
    printar_titulo('Editor de lista')
    opcoes = ['Adicionar anime da lista', 'Remover anime da lista', 'Voltar', 'Sair']
    printar_opcoes(opcoes)
    numero_opcao_escolhida = validar_opcao("Digite o número da sua opção --> ", len(opcoes))

    match numero_opcao_escolhida:
        case 1:
            adicionar_anime_na_lista(anime_list)
        case 2:
            remover_anime_da_lista(anime_list)
        case 3:
            menu_inicial()
        case 4:
            printar_titulo('Até a próxima! ;)')
        case _:
            editar_lista_de_animes()

# -------------------------------------------------------------------
# MENU SECUNDÁRIO - "Exibir detalhes dos animes"
# -------------------------------------------------------------------
def menu_exibir_detalhes_dos_animes(numero_opcao_escolhida_detalhes, anime_gerado_da_lista, anime_gerado_da_api):
    # Verifica qual opção de anime o usuário quer exibir as informações
    cls()
    if numero_opcao_escolhida_detalhes == 3:
        # Tratamento para ver se foi possível localizar o ID do anime
        resposta = (buscar_id_do_anime(anime_gerado_da_lista).split(':')[1])

        if not resposta.isnumeric:
            print(resposta)

        else:
            id_anime_gerado_lista = resposta
            printar_detalhes(gerar_informacao_do_anime_por_ID(id_anime_gerado_lista))
            printar_linha()
            printar_detalhes(anime_gerado_da_api)

    # Exibe as informações do anime 1 (Lista)
    elif numero_opcao_escolhida_detalhes == 1:
        # Tratamento para ver se foi possível localizar o ID do anime
        resposta = buscar_id_do_anime(anime_gerado_da_lista).split(':')[1]
        if not resposta.isnumeric:
            print(resposta)
        else:
            id_anime_gerado_lista = resposta
            printar_detalhes(gerar_informacao_do_anime_por_ID(id_anime_gerado_lista))

    # Exibe as informações do anime 2 (API)
    elif numero_opcao_escolhida_detalhes== 2:
        printar_detalhes(anime_gerado_da_api)

# -------------------------------------------------------------------
# FUNÇÕES DA LISTA DE ANIMES
# -------------------------------------------------------------------

def adicionar_anime_na_lista(anime_list):
    try:
        while True:
            cls()
            printar_titulo('Adicionador de animes')
            anime = input('Digite "2" para voltar ao menu '
                          '\n Ou digite o nome do anime que você quer adicionar --> ')
            if anime == "2":
                editar_lista_de_animes(anime_list)
                break

            # Verifica se o usuário não digitou apenas espaços ou deixou o nome do anime vazio
            if anime.isspace() or not anime:
                printar_entre_linhas('O programa não aceita nomes vazios')
                sleep(1)
                continue

            # Confirma o nome do anime
            print('"{}"'.format(anime))
            opcao = input('O nome do anime está correto? (S/N) --> ').upper()

            if opcao == 'S' or opcao == 'SIM':
                anime_list.append(anime)
                printar_entre_linhas('Anime {} adicionado com sucesso!'.format(anime))
                sleep(1)
                editar_lista_de_animes(anime_list)
                break

    except Exception:
        print('Erro, digite um nome válido')
        sleep(1)
        remover_anime_da_lista(anime_list)

def remover_anime_da_lista(anime_list):
    try:
        while True:
            cls()
            printar_titulo('Removedor de animes')
            printar_lista_de_animes(anime_list)
            anime = input('Digite "2" para voltar ao menu '
                            '\n Ou digite o nome do anime que você quer remover --> ')
            if anime == "2":
                editar_lista_de_animes(anime_list)
                break

             # Verifica se o usuário não digitou apenas espaços ou deixou o nome do anime vazio
            if anime.isspace() or not anime:
                printar_entre_linhas('O programa não aceita nomes vazios')
                sleep(1)
                continue

            # Confirma o nome do anime
            print('"{}"'.format(anime))
            opcao = input('O nome do anime está correto? (S/N) --> ').upper()

            if opcao == 'S' or opcao == 'SIM':
                anime_list.remove(anime.lower())
                printar_entre_linhas('Anime {} removido com sucesso!'.format(anime))
                sleep(3)
                remover_anime_da_lista(anime_list)
                break

    except ValueError:
        print('Erro, anime não encontrado na lista')
        sleep(2)
        remover_anime_da_lista(anime_list)

    except Exception:
        print('Erro, digite um nome válido')
        sleep(2)
        remover_anime_da_lista(anime_list)



if __name__ == '__main__':
    try:
        menu_inicial()
    except KeyboardInterrupt:
        print('\n\033[31m Execução Interrompida\033[m')
        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)
