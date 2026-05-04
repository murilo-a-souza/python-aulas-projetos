n = 0
x = 1
print('------------------------------\nSEQUÊNCIA DE FIBONACCI\n------------------------------')
qtd = int(input('Até que posição você quer ir? '))

print(f'------------------------------\nPosição\t| Valor')
for i in range(qtd):
    print(f'{i+1}\t| {n}')
    n, x = n+x, n
print(f'------------------------------\n')