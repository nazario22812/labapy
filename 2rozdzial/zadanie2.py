
list = []

for i in range(3):
    h = int(input(": "))
    if h>0:
        list.append(h)
    else: 
        input("Jeszcze raz: ")


for i in range(len(list)):
    cursor = list[i]
    pos = i

    while pos>0 and list[pos - 1] > cursor:
        list[pos] = list[pos - 1]
        pos = pos - 1
    
    list[pos] = cursor 
     

print(list[2])