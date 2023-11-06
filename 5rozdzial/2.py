roz = int(input("podaj rozmiar: "))
lat = []
n = 0
count = 0
suma = 0


for i in range(roz):
    n = int(input("> "))
    lat.append(n)

for b in lat:    
    if b > lat[-1]:
        suma += b
        count += 1
    else:
        pass
sred = suma/count

print(f"suma: {suma}\nsrednie: {sred}")