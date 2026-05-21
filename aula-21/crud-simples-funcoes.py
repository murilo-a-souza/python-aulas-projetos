'''
CRUD simples em memória (listas)
'''
#main list
alunos = []

#Create cadastrar aluno
def cadastrar():
    print('\n===================\nCADASTRAR ALUNO\n===================')
    nome = input('Digite o nome do aluno: ')
    if nome == '':
        print('Erro: nome inválido!')
        return
    alunos.append(nome)
    print('✅ Aluno cadastrado com sucesso!')

def listar():
    print('\n===================\nLISTRAR ALUNOS\n===================')
    if len(alunos) == 0:
        print('Nenhum aluno cadastrado!')
        return
    cont = 1
    for aluno in alunos:
        print(f'{cont} - {aluno}')
        cont += 1

def atualizar():
    print('\n===================\nATUALIZAR ALUNO\n===================')
    if len(alunos) == 0:
        print('Nenhum aluno cadastrado!')
        return
    listar()
    posicao = int(input('Diite o número do aluno: '))
    if posicao < 1 or posicao > len(alunos):
        print('Posição inválida!')
        return
    novo_nome = input('Novo nome: ')
    alunos[posicao-1] = novo_nome
    print('✅ Aluno atualizado com sucesso!')

def remover():
    print('\n===================\nREMOVER ALUNO\n===================')
    if len(alunos) == 0:
        print('Nenhum aluno cadastrado!')
        return
    listar()
    posicao = int(input('Diite o número do aluno: '))
    if posicao < 1 or posicao > len(alunos):
        print('Posição inválida!')
        return
    alunos.pop(posicao-1)
    print('✅ Aluno removido com sucesso!')

def menu():
    while True:
        opcao = int(input('''
===================
        CRUD
===================
1 - Cadastrar
2 - Listar
3 - Atualizar
4 - Remover  
0 - Sair  
                      
Escolha uma função: 
'''))
        match opcao:
            case 1:
                cadastrar()
            case 2:
                listar()
            case 3:
                atualizar()
            case 4:
                remover()
            case 0:
                print('Saindo do programa')
            case _:
                print('Valor inválido')
        if opcao == 0:
            return

#main menu
print('\n===================\nGESTÃO DE ALUNOS\n===================')
menu()
