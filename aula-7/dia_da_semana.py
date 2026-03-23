dia_semana = (input('Dia da semana: '))

match dia_semana:
    case 'Sábado' | 'Domingo':
        print(f'{dia_semana} é fim de semana!')
    case 'Segunda-Feira' | 'Terça-Feira' | 'Quarta-Feira' | 'Quinta-Feira' | 'Sexta-Feira':
        print(f'{dia_semana} é um dia útil! :/')
    case _:
        print('Dia da semana inválido!')