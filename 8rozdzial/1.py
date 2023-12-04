while True:
    def silnia(w):
        if w>=1:
            return w*silnia(w-1)
        else:
            return 1
        
    x = int(input("podaj liczbe: "))
    wynik = silnia(x)
    print(str(x)+'!='+str(wynik))