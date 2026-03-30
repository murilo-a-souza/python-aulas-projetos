executa = input('Executar o bloco? (sim-não) ')
contador = 0

while executa == 'sim': #Executa é a variável controladora
    contador += 1 #Contadora
    print('Dentro do WHILE!')
    executa = input('Você quer executar novamente? (sim-não)')
    if executa == 'não':
        break
print(f'O programa executou {contador} vezes')