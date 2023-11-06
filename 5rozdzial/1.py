lst = []
count = 0
suma = 0
check = False
koniec = 0

while koniec == 0:
    a = int(input(""))
    if a == 0:
        check = not(check)
    else:
        if check:
            suma += a
            count +=1
        else:
            if a<0:
                koniec +=1
            else:
                pass

if count>0:
    sred = suma / count
    print(f"Srednie: {int(sred)}")
else:
    print("Nie dodano zadnej liczby")