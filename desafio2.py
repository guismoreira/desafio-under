def calcula():
    matriz = [
        [27, 14, 6],
        [18, 11, 32],
        [4, 26, 15]
    ]
    somaP=0
    somaS=0

    cont1 = 0
    cont2 = len(matriz[0]) - 1

    for m in matriz:
        somaP += m[cont1]
        somaS += m[cont2]
        cont1 += 1
        cont2 -= 1

    print(abs(somaP - somaS))

calcula()