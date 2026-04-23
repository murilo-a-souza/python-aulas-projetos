'''
Crie um programa que receba como entrada quatro salários, calcule a média salarial e exiba os salários abaixo da médi
'''

salarios = [0, 0, 0, 0]
soma = 0
i = 0 #indice da lista
while i<4:
    salarios[i] = float(input('Salário: R$'))
    soma += salarios[i]
    i+=1
media = soma / 4
print(f'Média salarial: R${media:.2f}')
i=0 #indice da lista
while i<4:
    if salarios[i] < media:
        print(f'Salário abaixo da média: R${salarios[i]:.2f}')
    i+=1