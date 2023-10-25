list = []


def parz(array):
    n = len(list)
    for i in range(n // 2):
        if list[i] != list[n - i - 1]:        
            return False
    return True


# list1 = []
# list2 = [] 
count = 0
while True:
    n = int(input("> "))
    
    if n == 0:
        break
    else:
        list.append(n)

for i in list:
    count += 1

if count % 2 == 0:
    print(f"ilosc parzysta: {count}")
else:
    print(f"ilosc nieparzysta: {count}")

if parz(list):
    print("Tablica jest symetryczna")
else:
    print("Tablica nie jest symetryczna")

    
    
# print(f"{list[:int(count1)]}\n{list[int(count1):]}")

# if list[:int(count1)].count != list[int(count1):].count:
#     print("tablican nie jest symetryczna")
# else:
#     print("tablica jest symetryczna")
 