list = []

count = 0

while True:
    n = int(input("> "))
    if n == 0:
        break
    else:
        list.append(n)

for i in list:
    gl = list.count(i)
    count += gl

print(count)