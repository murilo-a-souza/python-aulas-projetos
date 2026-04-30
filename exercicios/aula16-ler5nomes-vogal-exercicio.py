nomes = []
vogais = []
consoantes = []

for i in range(5):
    nomes.append(input("Digite um nome: "))

print('\n=============== TODOS OS NOMES ===============')
for nome in nomes:
    print(nome)
    if (nome[0] == 'A') or (nome[0] == 'E') or (nome[0] == 'I') or (nome[0] == 'O')or (nome[0] == 'U'):
        vogais.append(nome)

    else:
        consoantes.append(nome)


print('\n============= COMEÇAM COM VOGAIS =============')
for nome in vogais:
    print(nome)
print(f'Quantidade de palavras iniciadas com vogal: {len(vogais)}')

print('\n=========== COMEÇAM COM CONSOANTES ===========')
for nome in consoantes:
    print(nome)
print(f'Quantidade de palavras iniciadas com consoantes: {len(consoantes)}')
