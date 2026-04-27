nomes = [] #lista vazia

for i in range(5):
    nome = input('Nome: ')
    nomes.append(nome)
print('\n------------------------------\n')
for nome in nomes:
    print(f'Nome: {nome}.')