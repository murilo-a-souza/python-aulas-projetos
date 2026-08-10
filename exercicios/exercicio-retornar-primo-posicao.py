def verifyPrimo(num : int, primos : list):
    if num < 2: return False
    for i in range(len(primos)):
        if num % primos[i] == 0: return False
    return num

def retornaPrimo(ind : int):
    num = 2
    primos = []
    while True:
        if verifyPrimo(num, primos):
            primos.append(num)
        if len(primos) == ind:
            break
        num += 1
    return primos[ind - 1]

print(retornaPrimo(int(input("Digite a posição do primo que você quer (1-x): "))))