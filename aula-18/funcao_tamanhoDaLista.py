'''
1. Função para obter o tamanho da lista
2. Função para preecher (popular) a lista
3. Função para imprimir os elementos da lista
4. Função para imprimir os elementos PARES da lista
5. Função para imprimir os elementos ÍMPARES da lista
'''
def tamanho_lista():
    print('---Tamanho da Lista---')    
    tamanho = int(input('Tamanho: '))
    return tamanho

def criar_lista(tamanho):
    print('---Criar lista---')
    lista = []
    i = 0
    while i <  tamanho:
        item = int(input('Item: '))
        lista.append(item)
        i+=1
    return lista

def imprimir(lista):
    print('---Imprimir lista---')
    for item in lista:
        print(f'Item: {item}')

def imprimir_pares(lista):
    print('---Imprimir pares da lista---')
    for item in lista:
        if item % 2 == 0:
            print(f'Item: {item}')

def imprimir_impares(lista):
    print('---Imprimir impares da lista---')
    for item in lista:
        if item % 2 != 0:
            print(f'Item: {item}')

def retorna_pares(lista):
    print('---Lista com os pares---')
    pares = []
    for item in lista:
        if item % 2 == 0:
            pares.append(item)
    return pares

def retorna_impares(lista):
    print('---Lista com os impares---')
    impares = []
    for item in lista:
        if item % 2 != 0:
            impares.append(item)
    return impares

            
# main
tamanho = tamanho_lista()
lista = criar_lista(tamanho)
imprimir(lista)
pares = retorna_pares(lista)
impares = retorna_impares(lista)
imprimir_pares(lista)
imprimir_impares(lista)
imprimir(impares)
imprimir(pares)