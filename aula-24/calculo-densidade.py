print('----- SISTEMA DE ANÁLISE DE MATERIAIS -----')

try:
    m = int(input('massa: '))
    v = int(input('volume: '))
    if v == 0 or m == 0:
        raise ValueError('Volume e massa não podem ser zero')
    if v < 0 or m < 0:
        raise ValueError('Volume ou massa não podem ser negativos')
    d = m / v
except ZeroDivisionError:
    print('Divisão por zero')
else:
    print('densidade: ', d)