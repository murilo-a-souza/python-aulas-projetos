'''
Escreva um programa em Python que leia 10 números o programa deve armazená-los em uma lista e na sequência imprimir apenas os números POSITIVOS.
'''
numeros = []
for i in range(1,11):
    numeros.append(int(input(f'Digite o {i}º número: ')))
print('---------------------\nPositivos:')
positivos = 0
for num in numeros:
    if num > 0:
        print(f'{num:.0f}.')
        positivos += 1
print('---------------------\nNegativos:')
negativos = 0
for num in numeros:
    if num < 0:
        print(f'{num:.0f}.')
        negativos += 1
print(f'---------------------\nHá {positivos} positivos no total!\nE {negativos} negativos no total!')