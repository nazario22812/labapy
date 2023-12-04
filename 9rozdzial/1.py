def znajdz_liczby_pierwsze(n):
    b = [True] * (n+1)
    b[0] = b[1] = False

    for i in range(2, int(n**0.5)+1):
        if b[i]:
            for j in range(i*i, n+1, i):
                b[j] = False

    b = [num for num in range(2, n+1) if b[num]]
    return b



n = int(input())
print(znajdz_liczby_pierwsze(n))
