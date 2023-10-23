nums = []
suma = 0
iloczyn = 1


while suma <= 255 and iloczyn <= 50000:
    n = int(input("wpisz czyslo: "))
    nums.append(n)
    suma =+ n

    iloczyn *= n

print(suma)
print(iloczyn)