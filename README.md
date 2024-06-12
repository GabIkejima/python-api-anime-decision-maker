<h1 align="center"><img  src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" height="185" width="185"><br />Anime Decision Maker</h1>

## Introdução

Sistema de menu interativo que consome a [API Jikan V.4](https://docs.api.jikan.moe/).

## Sobre
O sistema permite gerar animes aleatórios da API Jikan filtrando pelas notas maiores, também permite manter uma lista particular de animes para que o Decision Maker escolha entre eles. O sistema também conta com uma feature de tradução para pt/BR já que o conteúdo presente na API é em inglês/japonês.

<table>
  <tr>
    <td><img src="https://github.com/GabIkejima/python-api-anime-decision-maker/blob/main/assets/menu_principal.png" alt="Imagem do menu principal" style="width: 300 height : 200;"/></td>
    <td><img src="https://github.com/GabIkejima/python-api-anime-decision-maker/blob/main/assets/menu_anime.png" alt="Imagem do menu de animes" style="width: 300 height : 200;"/></td>
    <td><img src="https://github.com/GabIkejima/python-api-anime-decision-maker/blob/main/assets/lista_animes.png" alt="Imagem da lista de animes" style="width: 300 height : 200;"/></td>
    <td><img src="https://github.com/GabIkejima/python-api-anime-decision-maker/blob/main/assets/anime_descricao.png" alt="Imagem da descrição de um anime" style="width: 300 height : 400;"/></td>
  </tr>
</table>

### Funcionalidades 🛠
| Funcionalidade   | Descrição                                   |
| :---------- |:------------------------------------------ |
| `Menus`      | Os menus foram feitos utilizando o terminal, estilizados utilizando caracteres como "-", presentes em [interface.py](https://github.com/GabIkejima/python-api-anime-decision-maker/blob/main/interface.py)|
| `Requests`      | A API é consumida através de requests presentes em [requests.py](https://github.com/GabIkejima/python-api-anime-decision-maker/blob/main/request.py) |
| `Listas`      | A API atualmente conta com um sistema de armazenamento de informação via lists do python |

### Em desenvolvimento 🔧
As seguintes features estão em desenvolvimento!
- Integração com DB para persistência de dados
- Opção no menu para escolher idioma 
- Opção para filtro por "mood" no menu

## Dependências
Este projeto possui as seguintes dependências externas além das bibliotecas padrão do Python:
| Nome   | Versão | Descrição                                   |
| :---------- |:----|:------------------------------------------ |
| `googletrans`      | 4.0.0rc1 | Módulo utilizado do google translate (tradutor) para traduzir os textos de descrição de anime para pt/BR|
| `requests`      | 2.32.3 |Módulo utilizado para consumir os dados da API Jikan |

### Path to Awesome 🌟
Como instalar e utilizar o sistema:
1. **Clone o repositório:**
    ```bash
    git clone https://github.com/GabIkejima/python-api-anime-decision-maker.git
    ```
2. **Navegue até o diretório do projeto:**
    ```bash
    cd caminho/repositório
    ```
3. **[Opcional]Crie e ative um ambiente virtual Python:**
    Crie um ambiente virtual Python com o seguinte comando:
    ```bash
    python -m venv anime_api
    ```
    Em seguida, ative o ambiente virtual:

    - No Windows:

    ```bash
    anime_api\Scripts\activate
    ```

    - No macOS e Linux:

    ```bash
    source anime_api/bin/activate
    ```
4. **Instale as dependências:**
   Execute o seguinte comando para instalar todas as dependências necessárias:
    ```bash
    pip install -r requirements.txt
    ```
5. **Execute o sistema:**
    ```bash
    python app.py
    ```
    
## Tecnologias Utilizadas
![Python 3.11.9](https://img.shields.io/badge/Python-3.11.9-blue)
![Jikan API V.4](https://img.shields.io/badge/Jikan_API-V4-darkblue)

## Contribua com o projeto
[![Star](https://img.shields.io/github/stars/GabIkejima/sistema-bancario-python-dio?style=social)](https://github.com/GabIkejima/sistema-bancario-python-dio/stargazers)
[![Forks](https://img.shields.io/github/forks/GabIkejima/sistema-bancario-python-dio?style=social)](https://github.com/GabIkejima/sistema-bancario-python-dio/forks)
[![GitHub Issues](https://img.shields.io/github/issues/GabIkejima/sistema-bancario-python-dio?style=social)](https://github.com/GabIkejima/sistema-bancario-python-dio/issues/)

Sua contribuição é muito bem vinda! Formas que você pode contribuir:
1. Identificar e relatar bugs através do "Issues"🐛
2. Identificar e relatar possíveis melhorias⚠️
3. Adicionando o repositório aos favoritos (star)⭐
4. Modificando o código!🔧
   - Faça um fork do repositório.
   - Clone o fork localmente.
   - Crie uma nova branch a partir da branch main.
   - Faça suas alterações e adições de código na sua nova branch.
   - Faça o commit (comente as alterações).
   - Faça um push para sua branch no seu fork.
   - Vá para o repositório original e abra um Pull Request para a branch main.
   - Explique no Pull Request quais foram as mudanças realizadas.

## Histórico de versões

Version|Date|Comments
-------|----|--------
|1.0|Mar 14, 2023|Initial release|
|2.0|Jun 12, 2024|V2 release [Current]|


## Autores 

| [<img loading="lazy" src="https://avatars.githubusercontent.com/u/118475573?v=4" width=115><br><sub>Gabriel</sub>](https://github.com/gabIkejima)
| :---: 

<div align="center">-By <a href="https://github.com/gabIkejima">GabIkejima</a>-</div>
