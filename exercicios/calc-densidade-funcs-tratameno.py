def obter_massa():
    while True:
        try:
            m = int(input('Digite a massa (kg): '))
            if m < 0:
                raise ValueError('Massa não pode ser negativa')
        except ValueError as erro:
            print('[ERRO DE VALOR]: ', erro)
        else:
            return m

def obter_volume():
    while True:
        try:
            v = int(input('Digite o volume (kg): '))
            if v < 0:
                raise ValueError('Volume não pode ser negativa')
        except ValueError as erro:
            print('[ERRO DE VALOR]: ', erro)
        else:
            return v

def calcular_densidade(m: int, v:int):
    return m / v

def executar_analise():
    try:
        m = obter_massa()
        v = obter_volume()
        d = calcular_densidade(m, v)
    except ValueError as error:
        print('ERRO: ', erro)
    except ZeroDivisionError as error:
        print('ERRO de calculo, o divisor não pode ser zero')
    else:
        print('densidade: ', d)

executar_analise()