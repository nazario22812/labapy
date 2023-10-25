list = []

while True:
    n = int(input("> "))
    if n == 0:
        break
    else:
        list.append(n)

count = {value for value in list if list.count(value) > 2 }

print(count)

