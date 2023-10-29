while True:
    n = int(input("Podaj liczbę n (większą lub równą 4): "))
    if n >= 4:
        break
    else:
        print("Liczba musi być większa lub równa 4. Spróbuj ponownie.")

tablica = []
for i in range(n):
    element = int(input(f"Podaj element {i+1}: "))
    tablica.append(element)

max_sums = [float('-inf'), float('-inf')]
indices = [None, None]

for i in range(len(tablica)-2):
    for j in range(i+1, len(tablica)-1):
        for k in range(j+1, len(tablica)):
            current_sum = tablica[i] + tablica[j] + tablica[k]
            if current_sum > max_sums[0]:
                max_sums[1] = max_sums[0]
                indices[1] = indices[0]
                max_sums[0] = current_sum
                indices[0] = (i, j, k)
            elif current_sum > max_sums[1]:
                max_sums[1] = current_sum
                indices[1] = (i, j, k)

print(f"Największa suma trzech elementów wynosi: {max_sums[0]}")
print(f"Indeksy dla tej sumy to: {indices[0]}")
print(f"Druga największa suma trzech elementów wynosi: {max_sums[1]}")
print(f"Indeksy dla drugiej sumy to: {indices[1]}")