i = 0
tab = [] 
while i == 0:
    n = int(input("> "))
    if n % 10 == 0:
        i+=1
    else:
        tab.append(n)

suma = 0
count = 0
for i in tab:
    suma += i
    count+= 1

srednia = suma / count
tab.sort()
print(f"Najmniejszy element: {tab[0]}")
print(f"Srednie: {srednia}")

