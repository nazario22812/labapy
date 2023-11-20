lst = []
prawo = []
lewo = []


def jeden(n):
    lst.append(n)

def dwa():
    count = 0
    count2 = 0
    for i in lst:
        count+=1

    for i in lst:
        if i >2:
            count2+=1

    if count > count2:
        print("nie zaliczony")
    elif count == count2:
        print("zaliczony")

def trzy():
    count = 0
    suma = 0
    for i in lst:
        count+=1
    
    for i in lst:
        suma += i

    return suma/count

def cztery():
    

    for i in lst:
        if i > trzy():
            prawo.append(i)
        elif i < trzy():
            lewo.append(i)
    sorted = lewo + prawo
    print(sorted)

def piat():
    return lst

while True:
    n = int(input("> "))
    if n>=2 and n<=5:
        jeden(n)
    else:
        break    


dwa()
print(trzy())
print(cztery())
print(piat())