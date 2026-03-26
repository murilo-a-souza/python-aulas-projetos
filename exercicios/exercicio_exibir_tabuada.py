'''Escreva um programa em Python que solicite ao usuário a entrada de um número inteiro e, em seguida, exiba a tabuada desse número de 1 a 10.
O programa deve:
Ler um número informado pelo usuário utilizando a função input();
Converter o valor para inteiro;
Calcular e exibir os resultados das multiplicações desse número pelos valores de 1 até 10;
Apresentar a saída em um formato organizado, conforme o exemplo abaixo:
Exemplo de execução:
Digite um número: 5
Tabuada do 5:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 10 = 50
💡 Desafio adicional (opciona)'''

print('---------------------------------------------\nCalcular Taboada\n---------------------------------------------')

multiplicado = int(input('Qual número será multiplicado?: '))
multiplicador = int(input(f'Até qual número, {multiplicado}, será multiplicado?: '))
inicio = 1

if (multiplicado | multiplicador) <= 0: 
    print('Digite apenas inteiros positivos diferentes de 0!')
else:
    print(f'---------------------------------------------\nTaboada do {multiplicado}, multiplicando do 1 ao {multiplicador}\n---------------------------------------------')
    while inicio <= multiplicador:
        resultado = inicio * multiplicado
        print(f'{multiplicado} X {inicio} = {resultado}')
        inicio += 1
print('---------------------------------------------')