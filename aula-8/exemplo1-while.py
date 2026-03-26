'''
para inicio <= fim - Impirmir de forma creswcente os valores entre inicio e fim
para inicio > fim - Imprimir de forma decrescente os valores entre inicio e fim
'''
print('-----Exemplo 1 - While------')

inicio = int(input('Digite o número de ínicio: '))
fim = int(input('Digite o número final: '))

if inicio<fim:
    while inicio<=fim:
        print(f'Acrescentando, i: {inicio}.')
        inicio += 1
elif inicio>fim:
    while inicio>=fim:
        print(f'Diminuindo, i: {inicio}.')
        inicio -= 1
else:
    print('Eles são iguais')