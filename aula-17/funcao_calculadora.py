def menu():
    opcao = int(input('======= MENU =======\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n====================\n- Escolha uma opção:\n> '))
    return opcao

def entrada_dados():
    numero = int(input('- Digite um número:\n> '))
    return numero

def add(n1, n2):
    print('---- adição executada')
    return n1+n2

def sub(n1, n2):
    print('---- subtração executada')
    return n1-n2

def mult(n1, n2):
    print('---- multiplicação executada')
    return n1*n2

def div(n1, n2):
    print('---- divisão executada')
    return n1/n2

def imprimir(resultado):
    print(f'----------------------------\nResultado: {resultado}\n----------------------------')

def controlador(opcao, n1, n2):
    print('---- Carregando opção')
    match opcao:
        case 1:
            return add(n1, n2)
        case 2:
            return sub(n1, n2)
        case 3:
            return mult(n1, n2)
        case 4:
            return div(n1, n2)
        case _:
            print('Opção inválida')

print('----------------------------\nCALCULADORA\n----------------------------')
escolha = 'sim'
while escolha == 'sim':
    imprimir(controlador(menu(), entrada_dados(), entrada_dados()))
    escolha = input('> Gostaria de efetuar outra operação? sim/N\n> ')