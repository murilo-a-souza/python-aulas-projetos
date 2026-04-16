# inicio < fim -> Imprimir os elementos PARES
# inicio > fim -> Imprimir os elementos IMPARES
# inicio = fim -> imprimir uma mensagem "IGUAIS!"

# Permitir executar outras vezes

repete = 's'
while repete == 's':
    inicio = int(input('Inicio: '))
    fim = int(input('Fim: '))
    cont = 0
    if inicio < fim:
        while inicio<fim:
            if inicio%2==0:
                print(f'{inicio} é PAR!')
                cont += 1
            inicio+=1
        print(f'Quantidade de pares: {cont}')
    elif inicio > fim:
        while inicio>fim:
            if inicio%2!=0:
               print(f'{inicio} é IMPAR!')
               cont += 1
            inicio-=1
        print(f'Quantidade de impares: {cont}')
    else :
        print('Os números são IGUAIS!')
    repete = input('Deseja repetir? (s/n) ')

