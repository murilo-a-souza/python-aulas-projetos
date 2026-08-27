def calcular_medias(matriz:list):
    medias = []
    for linha in matriz:
        soma = sum(linha)
        medias.append(sum(linha)/len(linha))
    return medias

def mostrar_matriz(matriz:list):
    for linha in matriz:
        print(linha)

def mostrar_resultados(matriz: list, alunos:list):
    medias = media_sem_sum(matriz)
    for i in range(len(medias)):
        print(f'Aluno: {alunos[i]}\t|\tMédia: {medias[i]:.1f}')
    print('-------------\n')

def criar_matriz(alunos:list, n_notas:int):
    matriz = []
    for i in range(len(alunos)):
        n = []
        for j in range(n_notas):
            n.append(float(input(f'Digite a {j+1}º nota do aluno {alunos[i]}: ')))
        print('-------------')
        matriz.append(n)
    return matriz

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
    while True:
        aluno = input(f'Digite o nome do aluno ou \"fim\": ')
        if aluno == 'fim':
            return alunos
        alunos.append(aluno)

def remover_nomes(alunos:list):
    for i in range(len(alunos)):
        print(f'{i+1} - {alunos[i]}')
    while True:
        aluno = int(input(f'Digite o número do aluno para remover ou \"0\" para encerrar: '))
        if aluno == 0:
            return alunos
        alunos.pop(aluno-1)


def menu():
    print('--- Calculadora de Média ---\nRegistre alunos:')
    alunos = criar_nomes()
    while True:
        opcao = int(input(f'--- Calculadora de Média ---\n\nAlunos = {alunos}\n\n1. Registrar nomes\n2. Remover nomes\n3. Calcular média\n4. Sair\n\nDigite uma opção: '))
        match opcao:
            case 1:
                novos_nomes = criar_nomes()
                for aluno in novos_nomes:
                    alunos.append(aluno)
            case 2:
                alunos = remover_nomes(alunos)
            case 3:
                mostrar_resultados(criar_matriz(alunos, int(input('Digite quantas notas cada aluno terá: '))), alunos)
            case 4:
                return
            case _:
                print('----- Opção inválida!! -----')

menu()