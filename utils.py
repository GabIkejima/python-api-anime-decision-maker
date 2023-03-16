import random

def inserir_anime(anime_list, anime):
    try:
        anime_list.append(anime)
        response = 'anime "{}" adicionado com sucesso!'.format(anime)

    except Exception:
        response = 'Erro não identificado'
    return response


# Gerar o número correspondente da opção do anime
def gerar_anime_aleatorio(anime_list):
    numero_aleatorio = random.randint(0, len(anime_list)-1)
    while True:
        try:
            anime_aleatorio = anime_list[numero_aleatorio]
            break
        except IndexError:
            anime_aleatorio = anime_list[numero_aleatorio-1]
            continue
        except Exception:
            anime_aleatorio = anime_list[numero_aleatorio -1]
            continue
    return anime_aleatorio



