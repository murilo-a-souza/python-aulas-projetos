'''
Tarifa de estacionamento

Escreva um programa para calcular o valor a pagar em um estacionamento com base no tempo  de permanência:

Regras: 
- Até 1h -> R$5,00
- Até 2h -> R$8,00
- Até 3h -> R$10,00
- Acima de 3h - R$10,00 + R$2,00 por hora adicional

'''

horas = int(input('Quantas horas o veículo ficou estacionado?: '))

match horas:
    case 1:
        valor = float(5)
    case 2:
        valor = float(8)
    case 3:
        valor = float(10)
        if horas > 3:
            valor = valor + float(2 * (horas - 3))
    case _:
        print('Valor inválido.')

print(f'Esse carro ficou {horas}horas no estacionamento, então o custo dele ficou em: R${valor:.2f}.')