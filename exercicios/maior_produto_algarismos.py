def receber_numero(algarismos: str = '0'):
    algarismos = algarismos.strip()
    algDivs = list(algarismos)
    return algDivs

def encontrar_maior_produto(algDivs : list):
    produto = -1
    for x in range(len(algDivs)):
        algDivs[x] = int(algDivs[x])
        for y in range(x+1, len(algDivs)): #percorre a lista na posição 1
            algDivs[y] = int(algDivs[y])
            if algDivs[x] * algDivs[y] > produto:
                produto = algDivs[x] * algDivs[y]
                resultado = f"O maior produto entre os algarismos do número indicado é entre {algDivs[x]} e {algDivs[y]} cujo resultado é {produto}"
    return resultado

while True:
    algarismos = input("Irei encontrar o maior produto entre as multiplicações dos algarismos do número indicado, digite aqui (0 para encerrar):")
    if algarismos == "0":
        break
    print(encontrar_maior_produto(receber_numero(algarismos)))
    



