import os

restaurantes = ['Satoro','Italianinho', 'Spolleto', 'MCdonalds']

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def menu_return():
    print('Pressiona qualquer tecla para continuar...')
    input()
    main()

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando o app')

def opcao_invalida():
    exibir_subtitulo('Opção inválida. Tente novamente.')
    menu_return()

def cadastrar_restaurante():
    exibir_subtitulo('Cadastrar novo restaurante:\n')
    nome_restaurante = input('Nome do restaurante à cadastrar: ')
    restaurantes.append(nome_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!\n')
    menu_return()

def listar_restaurantes():
    exibir_subtitulo('Restaurantes cadastrados:')
    for restaurante in restaurantes:
        print(f'.{restaurante}')
    menu_return()


def ativar_restaurante():
    os.system('cls')

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1: 
            cadastrar_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            ativar_restaurante()
        elif opcao_escolhida == 4: 
            finalizar_app()
        else: 
             opcao_invalida()
    except ValueError:
        opcao_invalida()

def main():
    os.system('cls')  
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()