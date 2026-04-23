'''
Estrutura de repetição for

- Estrutura definida (qtde  de repetições conhecidas)
- Sintaxe:
    for <var> in <seq>:
        //bloco de código

- método append()
'''
# Solicite ao usuário o número de funcionários
# Altere os elementos da lista
# Imprimir os salários acima da média


salarios = []
soma = 0
numeroFuncionarios = int(input('Número de funcionários: '))

for i in range(numeroFuncionarios):
    salario = float(input('Salário: R$'))
    soma += salario
    salarios.append(salario)

media = soma / numeroFuncionarios
print('----------------------------------')
print(f'Média dos salários: R${media:.2f}')
print('----------------------------------')

# Armazenar em uma lista os salários acima da média
# Outra lista, porém pros abaixo da média 

acima_media  = []
abaixo_media = []

for salario in salarios:
    if salario < media:
        abaixo_media.append(salario)
    if salario > media:
        acima_media.append(salario)

if abaixo_media != []:
    print('Salários abaixo da média:')
    for i in abaixo_media:
        print(f'R${i:.2f}')
else:
    print('Não há salários abaixo da média')


if acima_media != []:
    print('Salários acima da média:')
    for i in acima_media:
        print(f'R${i:.2f}')
else:
    print('Não há salários acima da média')
