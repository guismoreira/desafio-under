def contPar(ar, num, k):
    freq = [0] * k

    for i in range(num):
        freq[ar[i] % k] += 1
    somaPar = freq[0] * (freq[0] - 1) / 2;
    i = 1

    while (i <= k // 2 and i != (k - i)):
        somaPar += freq[i] * freq[k - i]
        i += 1

    if (k % 2 == 0):
        somaPar += (freq[k // 2] * (freq[k // 2] - 1) / 2);

    return int(somaPar)


ar = [1, 3, 2, 6, 1, 2]
num = len(ar)
k = 3
print()
print(f'A soma dos pares divisíveis por {k} é {contPar(ar, num, k)}')
