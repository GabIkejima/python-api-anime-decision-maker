from time import sleep

def printar_linha(tam = 42):
    print ("-" * tam)

def printar_entre_linhas(frase):
    printar_linha()
    print(frase)
    printar_linha()
def printar_opcoes(opcoes, tipo='n'):
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

def printar_anime(anime):
    try:
        printar_linha()
        print('Minha sugestão de anime é: {}'.format(anime[0].upper() + anime[1:].lower()))
        printar_linha()
    except Exception:
        printar_entre_linhas('Erro ao localizar anime!')


