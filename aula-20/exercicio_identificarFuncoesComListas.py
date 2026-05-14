'''
Crie um programa em Python que permita cadastrar 5 nomes de jogos e uma lista. O programa deve mostrar todos os jogos cadastrados, permitindo também, adicionar e remover o nome de um jogo e ordenar a lista (jogos). Ao final, exiba a lista atualizada.
'''
def cadastrarJogos():
    print('===================================================================')
    print('CADASTRO DE JOGOS')
    print('===================================================================')
    jogos = []
    tamanho = int(input('Quantos jogos você quer cadastrar?: '))
    for i in range(tamanho):
        jogos.append(input(f'Digite o nome do {i+1}º jogo: '))
    print('Lista inicial:\n', jogos)
    return jogos

def addJogos(jogos):
    print('===================================================================')
    print('ADIÇÃO DE JOGOS')
    print('===================================================================')
    novo = input('Digite o nome do novo jogo, ou 0 para sair: ')
    while novo != '0':
        jogos.append(novo)
        print('Lista atual:\n', jogos)
        novo = input('Digite o nome do novo jogo, ou 0 para sair: ')
    return jogos

def removeJogos(jogos):
    print('===================================================================')
    print('REMOÇÃO DE JOGOS')
    print('===================================================================')
    jogo = input('Digite o nome do jogo à remover, ou 0 para sair: ')
    while jogo != '0':
        jogos.remove(jogo)
        print('Lista atual:\n', jogos)
        jogo = input('Digite o nome do jogo à remover, ou 0 para sair: ')
    return jogos

def ordenaJogos(jogos):
    print('===================================================================')
    print('ORDENAÇÃO DE JOGOS')
    print('===================================================================')
    opcao = int(input('Em qual ordem você que ordenar?\n1. Crescente (A-Z)\n2. Decrescente (Z-A)\n'))
    match opcao:
        case 1:
            jogos.sort()
            print('Lista atual:\n', jogos)
        case 2:
            jogos.sort(reverse=True)
            print('Lista atual:\n', jogos)
        case _:
            print('Opção inválida!')
    return jogos

def exibirJogos(jogos):
    print('===================================================================')
    print('EXIBIÇÃO DE JOGOS')
    print('===================================================================')
    for jogo in jogos:
        print(f'Jogo {jogos.index(jogo)+1} - {jogo}.')

jogos = []
while True:
    print('===================================================================')
    print('MENU DE JOGOS')
    print('===================================================================')
    opcao = int(input('Qual ação você gostaria de realizar?\n1. Cadastrar jogos.\n2. Adicionar jogos\n3. Remover jogos\n4. Ordenar jogos\n5. Exibir jogos\n0. Sair\n'))
    match opcao:
        case 1:
            jogos = cadastrarJogos()
        case 2:
            jogos = addJogos(jogos)
        case 3:
            jogos = removeJogos(jogos)
        case 4:
            jogos = ordenaJogos(jogos)
        case 5:
            exibirJogos(jogos)
        case _:
            if opcao != 0:
                print('Opção inválida!')
    if opcao == 0:
        break