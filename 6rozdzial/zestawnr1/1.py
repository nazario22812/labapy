tab = []
i = 0
count = 0


while i<4:
    n  = int(input("> "))
    if n > 0:    
        tab.append(n)
        i+=1
for b in tab:
    if count != 3: 
        dziel = b / tab[-1]
        count+=1
        print(int(dziel))
    else:
        break

print(tab)