valor_acumulado = 0
preco_item = 0

credito_disp = float(input('Quanto crédito você tem dsponível? '))

while True:
    valor_acumulado += preco_item
    preco_item = float(input('Digite o valor do item comprado: '))
    if credito_disp < preco_item:
        print('Você não tem saldo para este item!')
        break
    else:
        credito_disp -= preco_item

print(f'Crédito restante:\tR${credito_disp:.2f}\nValor total em compras:\tR${valor_acumulado:.2f}')