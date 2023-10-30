import random as r

lst = []
for i in range(6):
    g = r.randint(1, 40)
    lst.append(g)

print("wpisz 6 wartosci przez space")
ent = input().split()
st = [int(i) for i in ent]

count = 0
for i in lst:
    if int(i) in st:
        count+=1
    else:
        pass

print(lst)
print(st)

if count <=3:
    print("brak wygranej")
elif count == 4:
    print("wygrana 50 zł")
elif count == 5:
    print("wygrana 400 zł")
elif count == 6:
    print("wygrana 2000 zł")
