lista_compras = []

while True:
    item = input("Digite um item (ou 'sair') para FINALIZAR\n")
    if item.lower() == 'sair':
        break
    lista_compras.append(item)

print('\n ===== Lista de Compras =====')
for i in range(len(lista_compras)):
    print(f'{i+1}. {lista_compras[i]}')