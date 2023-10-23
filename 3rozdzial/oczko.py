import random

cards = {
    "2":2, "3":3, "4":4, 
    "5":5, "6":6, "7":7,
    "8":8, "9":9, "10":10,
    "walet":2, "dama":3, "krol":4, "as":11
}

p1 = []
p2 = []

for i in range(2):
    p1.append(random.choice(list(cards.values())))
    p2.append(random.choice(list(cards.values())))



p1_count = 0
p2_count = 0

def check():
    global p1_count, p2_count

    for i in p1:
        p1_count += int(i)

    for i in p2:
        p2_count += int(i)

    if p1_count < 22:
        return True

    elif p2_count < 22:
        return True

    else:
        return False

while True:

    while check():
        print(f"1) {p1}")
        put = int(input("1)0 - stop, 1 - add card\n> "))
        if put == 0:
            print(f"2) {p2}")
            gg = int(input("2)0 - stop, 1 - add card\n> "))
            if gg == 0:
                break
            elif gg == 1:
                p2.append(random.choice(list(cards.values())))
                print(f"2) {p2}\n")
        elif put == 1:
            p1.append(random.choice(list(cards.values())))
            print(f"1) {p1}\n")

        
        print(f"2) {p2}")
        put2 = int(input("2)0 - stop, 1 - add card\n> "))
        if put2 == 0:
            print(f"1) {p1}")
            gg = int(input("1)0 - stop, 1 - add card\n> "))
            if gg == 0:
                break
            elif gg == 1:
                p1.append(random.choice(list(cards.values())))
                print(f"1) {p1}\n")
        elif put2 == 1:
            p2.append(random.choice(list(cards.values())))
            print(f"2) {p2}\n")
    
    break


if p1_count == p2_count and p1_count < 22:
    print(f"remis\n1) {p1_count}\n2) {p2_count}")

elif p1_count > p2_count and p1_count < 22:
    print(f"pierwszy win\nwith {p1_count} points")

elif p2_count > p1_count and p2_count < 22:
    print(f"drugi win\nwith {p2_count} points")

else: 
    print("nikt nie wygral")