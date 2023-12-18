import time


oceny = [[],[],[],[],[]]


def indx_del(idx, przedmet):
    try:
        oceny[przedmet].pop(idx)
        print("ocena byla usunieta")
        print(f"oceny z danego przedmiotu\n{oceny[przedmet]}")

    except Exception:
        print("ocena nie byla usunieta")

def oglad(num):
    print(f"oceny danego z przedmiotu\n{oceny[num]}")

def check(num):
    if num >0 and num <6:
        return True


def ilosc(num):
    count = 0
    ilosc = []
    for i in oceny:
        for g in i:
            count+=1
        ilosc.append(count)
        count = 0

    return ilosc[num]


def dodawanie(numer, przedmiot):
    if ilosc(przedmiot) < 21:
        try:
            oceny[przedmiot].append(numer)
            print("ocena byla dodana")

        except Exception:
            print("ocena nie byla dodana")
    else:
        raise TypeError

while True:
    n = int(input("\ndodaj ocene\n1-wdi, 2-ni, 3-ps,\n4-md, 5-wdm, 6-pokaz tablice,\n7-usunac ocene, 0-exit: "))
    print("\n")
    match n:
        case 1:
            oc = int(input("> "))
            if check(oc):
                dodawanie(oc, 0)
            else:
                print("wprowadz poprawna ocene")
            
        case 2:
            oc = int(input("> "))
            if check(oc):
                dodawanie(oc, 1)
            else:
                print("wprowadz poprawna ocene")
        
        case 3:
            oc = int(input("> "))
            if check(oc):
                dodawanie(oc, 2)
            else:
                print("wprowadz poprawna ocene")
        
        case 4:
            oc = int(input("> "))
            if check(oc):
                dodawanie(oc, 3)
            else:
                print("wprowadz poprawna ocene")

        case 5:
            oc = int(input("> "))
            if check(oc):
                dodawanie(oc, 4)
            else:
                print("wprowadz poprawna ocene")

        case 6:
            print(oceny)

        case 7:
            k = int(input("z jakiego przedmiotu chcesz usunac ocene\n1-wdi, 2-ni,\n3-ps, 4-md,\n5-wdm: "))
            match k:
                case 1:
                    oglad(0)
                    ind = int(input("podaj index oceny dla usuniecia: "))
                    indx_del(ind,0)
                case 2:
                    oglad(1)
                    ind = int(input("podaj index oceny dla usuniecia: "))
                    indx_del(ind,1)
                
                case 3:
                    oglad(2)
                    ind = int(input("podaj index oceny dla usuniecia: "))
                    indx_del(ind,2)
                case 4:
                    oglad(3)
                    ind = int(input("podaj index oceny dla usuniecia: "))
                    indx_del(ind,3)
                case 5:
                    oglad(4)
                    ind = int(input("podaj index oceny dla usuniecia: "))
                    indx_del(ind,4)
        case 0:
            break

    time.sleep(2)