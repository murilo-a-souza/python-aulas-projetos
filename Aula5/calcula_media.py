'''
Escreva um algoritmo para calcular a média aritmética de três notas. 
O programa deve receber as três notas do usuário, calcular a média e apresentar o resultado.
'''

# Entrada de dados por atribuição

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
n3 = float(input('Nota 3: '))

# Processamento
media = ( n1 + n2 + n3 ) / 3

# Saída de dados
print("Média: ", media)