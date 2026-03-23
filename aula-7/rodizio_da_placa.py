'''
Escreva um programa em Python que leia um número, representando o final de uma placa (veículo) e verifique o dia do rodízio municipal.

-utilize a estrutura match-case para resolver o exercício.

Segunda-feira: 1 e 2
Terça-feira: 3 e 4
Quarta-feira: 5 e 6
Quinta-feira: 7 e 8
Sexta-feira: 9 e 0

'''

placa = int(input('Qual dígito final da sua placa?: '))

match placa:
    case 1 | 2:
        print('O dia do rodízio é Segunda-Feira')
    case 3 | 4:
        print('O dia do rodízio é Terça-Feira')
    case 5 | 6:
        print('O dia do rodízio é Quarta-Feira')
    case 7 | 8:
        print('O dia do rodízio é Quinta-Feira')
    case 9 | 0:
        print('O dia do rodízio é Sexta-Feira')
    case _:
        print('Inválido. Digite apenas um número.')