print('Exemplo 2 - While true - Repetição infinita')

i = 1
while True:
    print('Bom dia')
    i += 1
    if i == 10:
        continuar = input('Quer continuar? (s/n)')
        if continuar == 'n':
            break
        else:
            i = 1