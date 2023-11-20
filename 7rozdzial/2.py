list = []



def dodanie(g):
    list.append(g)

def usunieincie():
    list.pop(-1)

def wynik():
    return list




while True:
    n = int(input("> "))

    match n:
        case 1:
            g = int(input("dodaj liczbe do listy: "))
            dodanie(g)
        case 2:
            print("usuniencie jednej liczby")
            usunieincie()
        case 3:
            print(wynik())
        case 4:
            print("Stop")
            break
        