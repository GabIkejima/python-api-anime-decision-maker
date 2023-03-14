"""""
@autor
Gabriel Higa Ikejima
@version
1.0
@since
14 / 03 / 2023
"""

import os
import sys

from interface import *
from utils import *
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

anime_list = ['Naruto', 'haikyuu', 'one punch man', 'dbz']
anime_list = list(filter(None, anime_list))

def menu_inicial():
    cls()
    # Para adicionar, remover ou alterar alguma opção do menu, basta alterar o seguinte dicionário:
    lista_de_opcoes_menu = ['Escolha um anime por mim', 'Ver minha lista de animes', 'Editar minha lista de animes', 'Sair']

    printar_titulo("Olá, sou o ajudante de decisões v.01")
    printar_opcoes(lista_de_opcoes_menu)
    numero_opcao_escolhida_menu = validar_opcao("Digite o número da sua opção --> ", len(lista_de_opcoes_menu))

    # Direciona o usuário conforme a opção escolhida
    match numero_opcao_escolhida_menu:
        case 1:
            menu_animes()
        case 2:
            printar_lista_de_animes(anime_list)
            input('Digite qualquer coisa para continuar --> ')
            menu_inicial()
        case 3:
            editar_lista_de_animes(anime_list)
        case 4:
            printar_titulo('Até a próxima! ;)')
        case _:
            menu_inicial()

# Opção 1 do menu principal, para gerar um anime aleatório
def menu_animes():
    cls()
    # Para adicionar, remover ou alterar alguma opção do menu de anime, basta alterar o seguinte dicionário:
    lista_de_opcoes_anime = ['Gerar outro anime', 'Ver detalhes do anime', 'Voltar', 'Sair']
    numero_opcao_escolhida_anime = 1
    while (numero_opcao_escolhida_anime == 1):
        anime_gerado = gerar_anime_aleatorio(anime_list) # gera um anime aleatorio da lista de animes

        printar_anime(anime_gerado)
        printar_opcoes(lista_de_opcoes_anime)
        numero_opcao_escolhida_anime = validar_opcao("Digite o número da sua opção --> ", len(lista_de_opcoes_anime))

        match numero_opcao_escolhida_anime:
            case 1:
                continue
            case 2:
                printar_titulo('Detalhes do anime {}'.format(anime_gerado))
                input('Digite qualquer coisa para continuar --> ')
                menu_animes()
            case 3:
                menu_inicial()
            case 4:
                printar_titulo('Até a próxima! ;)')
                break
            case _:
                menu_animes()

# Opção 2 do menu principal, para mostrar os items da lista de animes
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

# Opção 3 do menu principal, para editar a lista de animes
def editar_lista_de_animes(anime_list):
    cls()
    printar_titulo('Editor de lista')
    opcoes = ['Adicionar anime da lista', 'Remover anime da lista', 'Voltar', 'Sair']
    printar_opcoes(opcoes)
    numero_opcao_escolhida = validar_opcao("Digite o número da sua opção --> ", len(opcoes))

    match numero_opcao_escolhida:
        case 1:
            printar_entre_linhas('Adicionar anime da lista')
        case 2:
            printar_entre_linhas('Remover anime da lista')
        case 3:
            menu_inicial()
        case 4:
            printar_titulo('Até a próxima! ;)')
        case _:
            editar_lista_de_animes()


if __name__ == '__main__':
    try:
        menu_inicial()
    except KeyboardInterrupt:
        print('\n\033[31m Execução Interrompida\033[m')
        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)
