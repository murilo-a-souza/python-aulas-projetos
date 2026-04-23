'''
Estrutura de repetição for

- Estrutura definida (qtde  de repetições conhecidas)
- Sintaxe:
    for <var> in <seq>:
        //bloco de código

- método append()
'''

salarios = [] #lista vazia
soma = 0
for i in range(4):
    salario = float(input('Salário: R$'))
    soma += salario
    salarios.append(salario)

media = soma / 4
print(f'Média dos salários: R${media:.2f}')

for salario in salarios:
    if salario < media:
        print(f'Abaixo da média: R${salario:.2f}')