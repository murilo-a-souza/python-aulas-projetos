nomes = []
vogais = []
consoantes = []
qtd_vogais = 0
qtd_consoantes = 0

for i in range(5):
    nomes.append(input("Digite um nome: "))

print('\n=============== TODOS OS NOMES ===============')
for nome in nomes:
    print(nome)
    if (nome[0] == 'A') or (nome[0] == 'E') or (nome[0] == 'I') or (nome[0] == 'O')or (nome[0] == 'U'):
        vogais.append(nome)
        qtd_vogais += 1
    else:
        consoantes.append(nome)
        qtd_consoantes += 1

print('\n============= COMEÇAM COM VOGAIS =============')
for nome in vogais:
    print(nome)
print(f'Quantidade de palavras iniciadas com vogal: {qtd_vogais}')

print('\n=========== COMEÇAM COM CONSOANTES ===========')
for nome in consoantes:
    print(nome)
print(f'Quantidade de palavras iniciadas com consoantes: {qtd_consoantes}')
