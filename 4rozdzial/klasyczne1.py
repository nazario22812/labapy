n = int(input("podaj n wartosc: "))

list = []

for i in range(n):
    ld = int(input("podaj czyslo: "))
    list.append(ld)


list.sort()
print(list[0,1])