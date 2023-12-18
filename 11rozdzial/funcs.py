import time

class Functional:
    oceny = [[],[],[],[],[]]
    
    def indx_del(self ,idx, przedmet):
        try:
            self.oceny[przedmet].pop(idx)
            print("ocena byla usunieta")
            print(f"oceny z danego przedmiotu\n{self.oceny[przedmet]}")
            time.sleep(2)
        except Exception:
            print("ocena nie byla usunieta")

    def oglad(self, num):
        print(f"oceny danego z przedmiotu\n{self.oceny[num]}")

    def check(self, num):
        if num >0 and num <6:
            return True


    def ilosc(self, num):
        count = 0
        ilosc = []
        for i in self.oceny:
            for g in i:
                count+=1
            ilosc.append(count)
            count = 0

        return ilosc[num]


    def dodawanie(self, numer, przedmiot):
        if self.ilosc(przedmiot) < 21:
            try:
                self.oceny[przedmiot].append(numer)
                print("ocena byla dodana")

            except Exception:
                print("ocena nie byla dodana")
        else:
            raise TypeError
        
    def srednia_all(self):
        suma = 0
        count = 0
        ilosc = []
        for i in self.oceny:
            for j in i:
                count += 1
                suma+=j
        result = suma/count
        ilosc.append(result)
        return ilosc
    
    def srednia_przedmiotu(self, przedmiot):
        suma = 0
        count = 0
        ilosc = []

        for i in self.oceny:
            for j in i:
                count+=1
                suma +=j
            try:
                result = suma/count
                ilosc.append(result)
                suma = 0
                count = 0
            except ZeroDivisionError:
                return "nie ma ocen z danego przedmiotu"
        return ilosc[przedmiot]

