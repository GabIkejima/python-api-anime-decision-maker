import random
from interface import *

anime_list = ['naruto', 'haikyuu', 'one punch man', 'dbz']

# Adicionar um anime na lista
def inserir_anime(anime):
    try:
        anime_list.append(anime)
        response = 'anime "{}" adicionado com sucesso!'.format(anime)

    except Exception:
        response = 'erro não identificado'
    return response
def consultar_animes():
    return anime_list

# Gerar o número correspondente da opção do anime
def gerar_numero_aleatorio():
    numero_aleatorio = random.randint(0, len(anime_list))
    return numero_aleatorio


def menu_inicial():
    # Para adicionar, remover ou alterar alguma opção do menu, basta alterar o seguinte dicionário:
    lista_de_opcoes = ['Escolha um anime por mim', 'Adicionar um anime na lista', 'Remover um anime da lista']

    printar_titulo("Ajudante de decisões v.01")
    printar_opcoes(lista_de_opcoes)
    numero_opcao_escolhida = validar_opcao("Digite o número da sua opção --> ", len(lista_de_opcoes))

    # Direciona o usuário conforme a opção escolhida
    match numero_opcao_escolhida:
        case 1:
            return "opcao escolhida 1"
        case 2:
            return "opcao escolhida 2"
        case 3:
            return "opcao escolhida 3"
        case _:
            menu_inicial()


print(menu_inicial())


