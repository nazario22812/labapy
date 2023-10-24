n = int(input("Podaj n: "))
array = []

for i in range(n):
    element = int(input(f"podaj czyslo: "))
    array.append(element)

start_range = int(input("podaj poczatek: "))
end_range = int(input("podaj koniec: "))

count = 0
for element in array:
    if start_range <= element <= end_range:
        count += 1

print(f"ilosc elementow w liscie {count}")
