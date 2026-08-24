def criar_matriz(alunos:list, n_notas:int):
    print('---------------------------------------\nRegistro de notas\n---------------------------------------\n')
    matriz = []
    for i in range(len(alunos)):
        n = []
        for j in range(n_notas):
            n.append(float(input(f'Digite a {j+1}º nota do aluno {alunos[i]}: ')))
        print('-------------')
        matriz.append(n)
    return matriz

def mostrar_resultados(notas: list, alunos:list):
    medias = media_sem_sum(notas)
    print('---------------------------------------\nMédias dos alunos\n---------------------------------------')
    for i in range(len(medias)):
        print(f'Aluno: {alunos[i]}\t|\tMédia: {medias[i]:.1f}')
    print('---------------------------------------\n')

def media_sem_sum(matriz:list):
    medias = []
    for linha in matriz:
        soma = 0
        for n in linha:
            soma += n
        medias.append(soma/len(linha))
    return medias

def criar_nomes():
    alunos = []
    print('---------------------------------------\nRegistro de nomes\n---------------------------------------\n')
    while True:
        aluno = input(f'Digite o nome do aluno ou \"fim\": ')
        if aluno == 'fim':
            return alunos
        alunos.append(aluno)
    print(n, '\n')

def mostrar_nomes(alunos:list):
    s = ''
    print('---------------------------------------\nExibição de nomes\n---------------------------------------\n')
    for n in alunos:
        s += f'- {n} '
    return s

def alterar_nomes(alunos:list):
    s = ''
    print('---------------------------------------\nAlteração de nomes\n---------------------------------------\n')
    for n in range(0,len(alunos)):
            s += f'{n+1}- {alunos[n]}\n'
    print(s)
    n = int(input('Digite o número do nome que você quer alterar: '))
    alunos[n-1] = input('Digite o novo nome: ')
    return alunos
    

def remover_nomes(alunos:list):
    print('---------------------------------------\nRemoção de nomes\n---------------------------------------\n')
    for i in range(len(alunos)):
        print(f'{i+1} - {alunos[i]}')
    while True:
        aluno = int(input(f'Digite o número do aluno para remover ou \"0\" para encerrar: '))
        if aluno == 0:
            return alunos
        alunos.pop(aluno-1)


def menu():
    print('---------------------------------------\nCalculadora de Média---------------------------------------\nRegistro inicial de alunos:\n')
    alunos = criar_nomes()
    notas = []
    while True:
        opcao = int(input(f'---------------------------------------\nCalculadora de Média---------------------------------------\n\nAlunos = {mostrar_nomes(alunos)}\n\n1. Registrar nomes\n2. Mostrar nomes\n3. Alterar nomes\n4. Remover nomes\n5. Registrar notas\n6. Calcular média e mostrar\n0. Sair\n\nDigite uma opção: '))
        match opcao:
            case 1:
                novos_nomes = criar_nomes()
                for aluno in novos_nomes:
                    alunos.append(aluno)
            case 2: 
                print(mostrar_nomes(alunos))
            case 3:
                alunos = alterar_nomes(alunos)
            case 4:
                alunos = remover_nomes(alunos)
            case 5:
                notas = criar_matriz(alunos, int(input('Digite quantas notas cada aluno terá: ')))
            case 6: 
                mostrar_resultados(notas, alunos)
            case 0: return
            case _: print('----- Opção inválida!! -----')


menu()