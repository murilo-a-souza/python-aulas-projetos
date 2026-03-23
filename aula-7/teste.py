dia_semana = int(input('Digite um número: '))

match dia_semana:
    case 1:
        print('Domingo!')
    case 2:
        print('Segunda-Feira!')
    case 3:
        print('Terça-Feira!')
    case 4:
        print('Quarta-Feira!')
    case 5:
        print('Quinta-Feira!')
    case 6:
        print('Sexta-Feira!')
    case 7:
        print('Sábado!')
    case _: #default
        print('Não é um dia de semana válido!')