'''
Calcula o IMC de uma pessoa.
- Leitura de peso e altura (uma ou duas funções)
- Calcula os dados
- Retorno dos dados
'''

def recebe_peso():
    while True:
        peso = float(input('Digite seu peso (em KG usando . para decimais): '))
        resp = input(f'Você confirma esse peso {peso}kg? (S/N)')
        if resp == 'S':
            break
    return peso

def recebe_altura():
    while True:
        altura = float(input('Digite sua altura (em metros usando . para decimais): '))
        resp = input(f'Você confirma essa altura {altura}m? (S/N)')
        if resp == 'S':
            break
    return altura

def recebe_idade():
    while True:
            idade = int(input('Digite sua idade: '))
            resp = input(f'Você confirma essa idade: {idade}? (S/N)')
            if resp == 'S':
                break
    return idade

def calcula_dados(peso, altura):
    imc = peso / (altura**2)
    print('O calculo do IMC de {peso} e {altura} é {imc}')
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        classificacao = "Baixo peso"
    elif imc >= 18.5 and imc < 24.99:
        classificacao = "Normal"
    elif imc >= 25 and imc < 29.99:
            classificacao = "Sobrepeso"
    elif imc >= 30:
            classificacao = "Obesidade"
    print('A classificação do IMC {imc} é {classificacao:.2f}')
    return classificacao

def menu():
    altura = 0 # essas variaveis servem mostrar os valores que são recebidos
    peso = 0
    idade = 0
    imc = 0
    classificacao = 'N/A'
    while True:
        opcao = int(input(f'--- Valores atuais ---\nPeso: {peso}\nAltura: {altura}\nIdade: {idade}\nIMC: {imc:.2f}\nClassificação: {classificacao}\n\n--- Menu de opções ---\nDigite uma opção:\n1. Obter peso\n2. Obter altura\n3. Registrar idade (opcional)\n4. Realizar Calculo\n5. Classificar IMC\n0. Sair\n'))
        match opcao:
            case 1:
                peso = recebe_peso()
                print('--------------------------------------')
            case 2:
                altura = recebe_altura()
                print('--------------------------------------')
            case 3:
                idade = recebe_idade()
                print('--------------------------------------')
            case 4:
                imc = calcula_dados(peso, altura)
                print('--------------------------------------')
            case 5:
                classificacao = classificar_imc(imc)
                print('--------------------------------------')
            case 0:
                print('Encerrando...')
            case _:
                print('Opção inválida')
                print('--------------------------------------')
        if opcao == 0:
            return

print('+++++++++ CALCULADORA DE IMC +++++++++')
menu()