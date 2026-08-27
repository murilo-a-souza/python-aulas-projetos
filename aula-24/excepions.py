try:
    n = int(input('Númerador:'))
    d = int(input('Denominador: '))
    r = n/d
except ValueError:
    print('entrada inválida!')
except ZeroDivisionError:
    print('Divisã por zero não permitida!')
else:
    print('resultado:', r)
finally:
    print('encerrando')