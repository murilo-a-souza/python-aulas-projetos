'''
Escreva um programa em Python para calcular a comissão de vendas de um vendedor de peças. 
O programa deve obter o ID do vendedor, a quantidade de peças vendidas e o valor unitário de cada peça.
Ao final, o programa deve calcular o otal vendido pelo vendedor e aplicar 5% de comissão sobre o total.

O programa deve:
- Obter os dados de entrada
- Calcular o total vendido e a comissão (5%)
- Apresentar os dados de saída
'''

idVendedor = int(input('Digite o ID do vendedor: '))
qtdePecas = int(input('Digite quantas peças esse vendedor vendeu: '))
valorPecas = int(input('Digite o valor unitário das peças vendidas: R$'))
comissao = (valorPecas*qtdePecas)*0.05

print('\nID:\t\t\t\t', idVendedor, '\nQtde. de peças vendidas:\t', qtdePecas, '\nValor das peças:\t\tR$', valorPecas, '\nValor da comissão:\t\tR$', comissao)