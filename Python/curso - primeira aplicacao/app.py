import os
import sys
import time

restaurantes = [
    {'nome':'Bebeto',
    'categoria':'Pizzaria',
    'ativo':True},
    
    {'nome':'Dalvino',
    'categoria':'Pizzaria',
    'ativo':False}]

def apresentacao():
    print("""Sabor Expresso

    1. Cadastrar Restaurante
    2. Listar Restaurante
    3. Ativar Restaurante
    4. Sair
    """)

def alterar_estado_restaurante():
    iniciar_menu('Alterando o status de ativação do restaurante')

    nome_restaurante = input('Digite o nome do restaurate que deseja alterar o estado: ')
    restaurante_encontrado = False

    for i in restaurantes:
        if nome_restaurante == i['nome']:
            restaurante_encontrado = True
            i['ativo'] = not i['ativo']
            msg = f'O restaurante foi {nome_restaurante} foi ativado com sucesso.' if i['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso.'
            print(msg)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')
    voltar_ao_menu()


def finalizar_app():
    for i in range(5):
        os.system('cls')
        print("Finalizando o programa.  ")
        time.sleep(0.33)
        os.system('cls')
        print("Finalizando o programa . ")
        time.sleep(0.33)
        os.system('cls')
        print("Finalizando o programa  .")
        time.sleep(0.33)

def listar_restaurantes():
    iniciar_menu('Listando todos os restaurantes')
    for i in restaurantes:
        nome_restaurante = i['nome']
        categoria = i['categoria']
        ativo = 'ativo' if i['ativo'] else 'desativado'
        print(f'· Restaurante: {nome_restaurante} da categoria {categoria} está {ativo}')
    voltar_ao_menu()

def iniciar_menu(texto):
    os.system('cls')
    print(texto)

def voltar_ao_menu():
    input('\nDigite uma tecla para voltar ao menu principal. ')
    main()

def opcao_invalida():
    print('Opção inválida"\n')
    voltar_ao_menu()

def cadastro_novo():
    iniciar_menu('Realizando cadastro\n')
    nome_restaurante = input('Digite o nome do restaurante: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_restaurante}: ')
    dados_restaurante = {'nome':nome_restaurante,'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_restaurante)
    voltar_ao_menu()

def opcao():
    try:
        op_escolhida = int(input("Escolha uma opção: "))
        match op_escolhida:
            case 1:
                cadastro_novo()
            case 2:
                listar_restaurantes()
            case 3:
                alterar_estado_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    apresentacao()
    opcao()

if __name__ == '__main__':
    main()