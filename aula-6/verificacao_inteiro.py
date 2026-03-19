'''
Escreva um programa que receba um número inteiro, verifique se ele é negativo, positivo ou neutro. 
O programa deve exibir uma mensagem ao usuário.
'''

#Entrada de dados
n = int(input('Digite um número inteiro: '))

#Aninhadas
if n > 0:
    input('Esse número é positivo.')
elif n < 0:
    input('Esse número é negativo')
else:
    input('Esse número é neutro (0)')