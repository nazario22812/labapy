print("Witaj w grze Papier, nożyce, kamień!")

count1 = 0
count2 = 0

def check():
    global count1, count2
    
    if count1 >= 3 or count2 >= 3:
        return False
    
    else:
        return True
    
# while check:
while check():
    p1 = int(input("Gracz 1, wybierz (0 - papier, 1 - nożyce, 2 - kamień): "))
    p2 = int(input("Gracz 2, wybierz (0 - papier, 1 - nożyce, 2 - kamień): "))


    if (p1 == 0 and p2 == 1) or (p1 == 1 and p2 == 2) or (p1 == 2 and p2 == 0):
        count2 += 1
        print(f"Gracz2 + 1 point\nrachunek {count1}:{count2}")

    elif (p2 == 0 and p1 == 1) or (p2 == 1 and p1 == 2) or (p2 == 2 and p1 == 1):
        count1 += 1
        print(f"Gracz1 + 1 point\nrachunek {count1}:{count2}")
    elif p1 == p2:
        print("remis")
        continue
    
    # break

if count1 > count2:
    print("Gracz 1 win")

elif count2 > count1:
    print("Gracz 2 win")