import random

lst = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8]
random.shuffle(lst)

count = 8
licznik = 0

while count > 0:
    
    print("podaj dwa indeksa tablicy przez space 0-15")
    ent = input().split()
    st = [int(i) for i in ent]

    a = lst[st[0]]
    b = lst[st[1]]
    
    #print(lst)
    print(f"{a} i {b}")

    if a == b:
        lst[st[0]] = 0
        lst[st[1]] = 0
        count =-1
        licznik += 1
        #print(lst)

    else:
        continue
print("Ty wygrales")


#print(lst)
