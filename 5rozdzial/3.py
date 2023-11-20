n = int(input("podaj n: "))
i = 0
tab= []

while i<n:
    b = int(input("> "))
    tab.append(b)
    i+=1

i = 0
suma = 0
liczbael = 0
ostatni = tab[-1]

while i<n:
    if tab[i] > ostatni:
        suma += tab[i]
        liczbael += 1
    i+=1

if liczbael > 0:
    srednia = suma / liczbael
    print(f"Suma warunku: {suma}")
    print(f"Srednia wynosi: {srednia}")
else:
    print("Zaden element nie spelnia warunku")
