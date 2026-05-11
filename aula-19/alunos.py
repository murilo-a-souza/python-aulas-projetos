'''
funções:
1- qtde_alunos()
2- notas_alunos()
3- imprimir_notas()
5- calc_mediaNotas()
6- qtde_abaixoMedia()
7- imprimi_abaixoMedia()
'''
def qtde_alunos():
    print('---Qtde. de Alunos')
    qtde = int(input('Qtde.: '))
    return qtde
def notas_alunos(qtde):
    print('---Notas dos alunos')
    notas = []
    for i in range(qtde):
        notas.append(float(input('Nota: ')))
    return notas
def imprimir_notas(notas):
    print('---Relatório de notas')
    print('Notas: ', notas)
    print('---------------------')
    for nota in notas:
        print(f'Nota: {nota:.1f}')
def calc_mediaNotas(notas):
    print('---Média das notas')
    soma = 0
    for nota in notas:
        soma += nota
    return soma / len(notas)
def qtde_abaixoMedia(notas, media):
    print('---Qtde. Abaixo da média')
    qtde_abaixoMedia = 0
    for nota in notas:
        if nota < media:
            qtde_abaixoMedia += 1
    return qtde_abaixoMedia
def imprimir_abaixoMedia(notas, media):
    print('Imprimir notas abaixo da média')
    for nota in notas:
        if nota < media:
            print('Abaixo da média: ', nota)

#main

qtde = qtde_alunos()
notas = notas_alunos(qtde)
imprimir_notas(notas)
media = calc_mediaNotas(notas)
print('Média: ', media)
abaixo_media = qtde_abaixoMedia(notas, media)
print(f'Notas abaixo da média: ', abaixo_media)
imprimir_abaixoMedia(notas,media)