n = int(input("podaj rozmiar: "))
i = 0
tab = []

while i < n:
    b = int(input("> "))
    tab.append(b)    
    i += 1

przesun = 0
i = 0
while i < n:
    if tab[i] != 0 and tab[i] % 5 == 0:
        przesun = przesun + 1
    else: 
        tab[i-przesun] = tab[i]
    i+=1


i = 0 
while i<n-przesun:
    print(tab[i])
    i+=1

