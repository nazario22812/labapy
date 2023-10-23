inp = int(input("> "))
suma = 0
count = 0

setki = ["0"]
dziesiatki = ["0"]
jednosci = ["0"]

if inp >= 0 and inp <= 999:
    a = "" + str(inp)
    for i in a:
        count += 1

    if count == 1:
        jednosci.insert(0 ,a[0])

        suma = int(jednosci[0])
    
    elif count == 2:
        dziesiatki.insert(0 ,a[0])
        jednosci.insert(0 ,a[1])

        suma = int(dziesiatki[0]) + int(jednosci[0])

    elif count == 3:
        setki.insert(0 ,a[0])
        dziesiatki.insert(0 ,a[1])
        jednosci.insert(0 ,a[2])

        suma = int(setki[0]) + int(dziesiatki[0]) + int(jednosci[0])       
    

    print(f"Suma cyfr: {suma}, setki: {setki[0]}, dziesiatki: {dziesiatki[0]}, jednosci: {jednosci[0]}")

else:
    print("Błąd")