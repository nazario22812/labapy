n = int(input("podaj n wartosc: "))

list = []

for i in range(n):
    ld = int(input("podaj czyslo: "))
    list.append(ld)


list.sort()
list.reverse()
print(f"1.{list[0]}\n2.{list[1]}")