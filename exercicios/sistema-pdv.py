# Sistema de PDV (Ponto de Venda) Simples
# 
# Desenvolva um programa que simule o fechamento de uma compra em um caixa de supermercado. O programa deve processar a entrada de preços de diversos produtos (valores decimais) e acumulá-los em uma variável de subtotal.
# Requisitos:
# O programa deve utilizar uma estrutura de repetição para receber os preços um a um.
# Para sinalizar o encerramento da entrada de dados (condição de parada), o usuário deverá digitar o valor -1.
# Após a inserção do valor de parada, o programa deve exibir o valor total da compra formatado com duas casas decimais.
# Certifique-se de que o valor de sentinela (-1) não seja somado ao total final.

preco = 0
valor_final = 0
while preco >= 0:
    valor_final += preco
    preco = float(input('Digite o preço do produto (-1 para finalizar): '))
print(f'\n------------------------------------\nValor total da compra: R${valor_final:.2f}\n------------------------------------\n')