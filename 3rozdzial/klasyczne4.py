# Inicjalizacja zmiennych
even_number = True
numbers = []

# Pobieranie od użytkownika wartości do momentu podania liczby nieparzystej
while even_number:
    number = int(input("Podaj liczbę: "))
    if number % 2 != 0:
        even_number = False
    else:
        numbers.append(number)

# Wyznaczanie najmniejszej i największej wartości
min_value = min(numbers)
max_value = max(numbers)

# Inicjalizacja zmiennej wynikowej
result = 1

# Obliczanie potęgi w oparciu o pętlę
for _ in range(max_value):
    result *= min_value

# Wyświetlanie wyniku
print(f"Wynik potęgowania to: {result}")
