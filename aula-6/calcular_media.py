'''
Escreva um programa em Python que calcule a média aritmética de três notas. O programa deve receber as três notas do usuário, calcular a média e apresentar o resultado, e verificar se aluno foi aprovado ou não.
'''

#Entrada de dados

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
n3 = float(input('Nota 3: '))

#Processamento
media = (n1+n2+n3)/3

#Saida de dados
print('Média: ', media)

#Verificação do status do aluno (teste)
if media >= 6:
    print('Aprovado!')
else:
    print('Reprovado!')