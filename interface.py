from time import sleep

def printar_linha(tam = 42):
    print ("-" * tam)

def printar_opcoes(opcoes):
    c = 1
    for opcao in opcoes:
        print(f'{c} - {opcao}')
        c += 1

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
            sleep(1)
    return opcao
