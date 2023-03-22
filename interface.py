from time import sleep
from interface import *
import textwrap
def printar_linha(tam = 42):
    print ("-" * tam)

def printar_entre_linhas(frase):
    printar_linha()
    print(frase)
    printar_linha()
def printar_opcoes(opcoes: object, tipo: object = 'n') -> object:
    c = 1
    if tipo == 'n':
        for opcao in opcoes:
            print(f'{c} - {opcao[0].upper()+opcao[1:]}')
            c += 1
    elif tipo == '*':
        for opcao in opcoes:
            print(f'*  {opcao[0].upper()+opcao[1:]}')
    elif tipo == '#':
        for opcao in opcoes:
            print(f'# {opcao[0].upper()+opcao[1:]}')

def printar_titulo(frase):
    printar_linha()
    print(frase.center(42))
    printar_linha()

def validar_opcao(frase, quantidade_de_opcoes):
    while True:
        try:
            opcao = int(input(frase))
            if opcao > quantidade_de_opcoes or opcao < 1:
                print("Opção inexistente, digite uma opção válida!")
                continue
            break
        # Tratamento de exceções
        except ValueError:
            print("Opção inválida, digite um número inteiro!")
            continue
        except Exception:
            print("ERRO na escolha das opções")
            continue
        finally:
            sleep(0.5)
    return opcao

def printar_anime(anime, frase):
    try:
        print('{} {}'.format(frase, anime[0].upper() + anime[1:].lower()))
    except Exception:
        printar_entre_linhas('Erro ao localizar anime!')


def printar_detalhes(anime):
    printar_titulo('Detalhes do anime {}'.format(anime['titulo']))
    print('Ano - ', anime['ano'])
    print('Nota - ', anime['nota'])
    texto = 'Sinopse - ' + anime['sinopse']
    print(textwrap.fill(texto, width=70))