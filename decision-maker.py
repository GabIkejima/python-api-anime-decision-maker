import random


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
    while True:
        print("Bem-vindo ao seu ajudante de decisões!")
        print(" 1 - Escolha um anime pra mim!")
        print(" 2 - Adicionar um anime na lista")
        print(" 3 - Remover um anime da lista")

        try:
            opcao = int(input("Digite o número da opção -> "))
            if opcao > 3 or opcao < 1:
                print("Número de opção inexistente, digite uma opção válida!")
                continue
            break
        # Tratamento de exceções
        except ValueError:
            print("Opção inválida, digite um número válido!")
            continue
        except Exception:
            print("Erro na escolha das opções")
            continue
            
        # Direciona o usuário conforme a opção escolhida
    match opcao:
        case 1:
            return "opcao escolhida 1"
        case 2:
            return "opcao escolhida 2"
        case 3:
            return "opcao escolhida 3"
        case _:
            menu_inicial()


print(menu_inicial())


