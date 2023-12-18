import time
from funcs import Functional
import os


d = Functional()

while True:
    n = int(input("\ndodaj ocene\n1-wdi, 2-ni, 3-ps,\n4-md, 5-wdm, 6-pokaz tablice,\n7-usunac ocene, 8-srednia\n0-exit: "))
    # print("\n")
    match n:
        case 1:
            oc = int(input("> "))
            if d.check(oc):
                d.dodawanie(oc, 0)
            else:
                print("wprowadz poprawna ocene")
            time.sleep(0.3)
            os.system("cls")
        case 2:
            oc = int(input("> "))
            if d.check(oc):
                d.dodawanie(oc, 1)
            else:
                print("wprowadz poprawna ocene")
            time.sleep(0.3)
            os.system("cls")
        case 3:
            oc = int(input("> "))
            if d.check(oc):
                d.dodawanie(oc, 2)
            else:
                print("wprowadz poprawna ocene")
            time.sleep(0.3)
            os.system("cls")
        case 4:
            oc = int(input("> "))
            if d.check(oc):
                d.dodawanie(oc, 3)
            else:
                print("wprowadz poprawna ocene")
            time.sleep(0.3)
            os.system("cls")        
        case 5:
            oc = int(input("> "))
            if d.check(oc):
                d.dodawanie(oc, 4)
            else:
                print("wprowadz poprawna ocene")
            time.sleep(0.3)
            os.system("cls")
        case 6:
            print(d.oceny)
            time.sleep(3)
            os.system("cls")
        case 7:
            k = int(input("z jakiego przedmiotu chcesz usunac ocene\n1-wdi, 2-ni,\n3-ps, 4-md,\n5-wdm: "))
            match k:
                case 1:
                    d.oglad(0)
                    ind = int(input("podaj index oceny dla usuniecia: "))
                    d.indx_del(ind,0)
                    os.system("cls")
                case 2:
                    d.oglad(1)
                    ind = int(input("podaj index oceny dla usuniecia: "))
                    d.indx_del(ind,1)
                    os.system("cls")
                case 3:
                    d.oglad(2)
                    ind = int(input("podaj index oceny dla usuniecia: "))
                    d.indx_del(ind,2)
                    os.system("cls")
                case 4:
                    d.oglad(3)
                    ind = int(input("podaj index oceny dla usuniecia: "))
                    d.indx_del(ind,3)
                    os.system("cls")
                case 5:
                    d.oglad(4)
                    ind = int(input("podaj index oceny dla usuniecia: "))
                    d.indx_del(ind,4)
                    os.system("cls")
        
        case 8:
            b = int(input("wybierz jaka chcesz srednia\n1-ze wszystkich predmiotow\n2-z jednego przedmiotu: "))    
            match b:    
                case 1:
                    print(f"srednia ze wszystkich przedmiotow: {d.srednia_all()}")
                    time.sleep(2)
                    os.system("cls")
                case 2:
                    kak = int(input("z jakiego przedmiotu chcesz wznac srednia\n1-wdi, 2-ni,\n3-ps, 4-md,\n5-wdm: "))
                    match kak:
                        case 1:
                            print(f"srednia z przedmiotu wdi: {d.srednia_przedmiotu(0)}")
                            time.sleep(2)
                            os.system("cls")
                        
                        case 2:
                            print(f"srednia z przedmiotu ni: {d.srednia_przedmiotu(1)}")
                            time.sleep(2)
                            os.system("cls")
                        
                        case 3:
                            print(f"srednia z przedmiotu ps: {d.srednia_przedmiotu(2)}")
                            time.sleep(2)
                            os.system("cls")
                        
                        case 4:
                            print(f"srednia z przedmiotu md: {d.srednia_przedmiotu(3)}")
                            time.sleep(2)
                            os.system("cls")
                        
                        case 5:
                            print(f"srednia z przedmiotu wdm: {d.srednia_przedmiotu(4)}")
                            time.sleep(2)
                            os.system("cls")
        case 0:
            break
    