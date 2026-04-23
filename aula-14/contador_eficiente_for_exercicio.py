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

print(f'Salários abaixo da média:')
for salario in salarios:
    if salario < media:
        print(f'R${salario:.2f}')

print(f'Acima da média:')
for salario in salarios:
    if salario > media:
        print(f'R${salario:.2f}')

# Armazenar em uma lista os salários acima da média
# Outra lista, porém pros abaixo da média