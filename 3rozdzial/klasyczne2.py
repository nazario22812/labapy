n = int(input("podaj n: "))
nums = []
suma = 0

for i in range(n):
    lic = int(input("Wpisz czyslo od 10 do 50: "))
    if 10 <= lic <= 50:
        nums.append(lic)
    else:
        pass

for i in nums:
    suma += i**2

print(suma)