'''
Calculo da conta de energia 2026. Escreva um programa paa calcular a conta de energia elétrica de um consumidor com base em kWh. O programa deve receber o consumo e calcular o valor a ser pago. Ao final, deve imprimir a conta detalhada (consumo, tarifa aplicada, valor a ser pago).

Regras do negócio:
1. Consumo  < 150 kWh: R$0,75 por kWh
2. Consumo entre 150 e 500kWh: R$0,95 por kWh
3. Consumo acima de 500kWh: R$1,20
Taxa Mínima (Disponibilidade): R$45,00 (Se o calculo do consumo for menor que R$45,00, o valor a ser pago será R$45,00)
'''

input('------Calculador de Energia 2026------\n(Digite qualquer tecla para continuar)')

consumo_kWh = float(input('Consumo em kWh: '))

if consumo_kWh < 150:
    valorBase = consumo_kWh * 0.75
    faixa = 'Baixo consumo'
elif (consumo_kWh >= 150) and (consumo_kWh < 500):
    valorBase = consumo_kWh * 0.95
    faixa = 'Médio consumo'
else:
    valorBase = consumo_kWh * 1.20
    faixa = 'Alto consumo'

if valorBase < 45:
    valorFinal = 45
    tarifa = 'Tarifa mínima aplicada'
else:
    valorFinal = valorBase
    tarifa = 'Tarifa mínima não aplicada'

print('Seu consumo total foi:\t\t\t', consumo_kWh, 'khW\nVocê ficou na faixa de preços:\t\t', faixa, '\nTarifa aplicada:\t\t\t', tarifa, '\nValor a ser pago:\t\t\t R$',valorFinal)