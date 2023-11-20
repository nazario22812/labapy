n = input().split()
tab = [int(i) for i in n]

suma = 0

for i in tab:
    kwadrat = i**2
    suma+=kwadrat

print(suma)