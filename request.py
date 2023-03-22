import requests
import random
import utils
def gerar_informacao_do_anime_por_ID(id = random.randint(0, 500)):
    while True:
        url = 'https://api.jikan.moe/v4/anime/{}'.format(id)
        anime = {
            'titulo': '',
            'genero': '',
            'ano': '',
            'nota': '',
            'sinopse': ''
        }

        response = requests.get(url=url, timeout = 2)


        if response.status_code >= 200 and response.status_code <= 299:
            # Sucesso
            response_data = response.json()

            try:
                for generos in response_data['data']['genres']:
                    anime['genero'] += ', ' + generos['name']
                anime['genero'] = anime['genero'][2:]
            except Exception:
                anime['genero'] = 'Gênero não informado'

            anime['titulo'] = response_data['data']['title']
            anime['ano'] = response_data['data']['year']
            anime['nota'] = response_data['data']['score']
            anime['sinopse'] = utils.traduzir_texto(response_data['data']['synopsis'])

            # Verifica se os campos da resposta da API estão preenchidos com alguma informação
            if not anime['titulo']:
                continue
            else:
                if not anime['ano']:
                    anime['ano'] = 'Ano não informado'

                if not anime['nota']:
                    anime['nota'] = 'Nota não informada'

                if not anime['sinopse']:
                    anime['sinopse'] = 'Sinopse não informada'

            return(anime)

        else:
            id_novo = random.choice([i for i in range (1, 500) if i != id])
            id = id_novo
            continue

def ver_detalhe_do_anime(anime):
    while True:

        return "detalhes do {}".format(anime)