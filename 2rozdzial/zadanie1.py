print("Witaj w grze Papier, nożyce, kamień!")

# Gracz 1 wybiera symbol
while True:
    player1 = input("Gracz 1, wybierz (0 - papier, 1 - nożyce, 2 - kamień): ")
    if player1 in ['0', '1', '2']:
        break
    else:
        print("Niepoprawny symbol. Spróbuj jeszcze raz.")

# Gracz 2 wybiera symbol
while True:
    player2 = input("Gracz 2, wybierz (0 - papier, 1 - nożyce, 2 - kamień): ")
    if player2 in ['0', '1', '2']:
        break
    else:
        print("Niepoprawny symbol. Spróbuj jeszcze raz.")

# Sprawdzenie wyniku
if player1 == player2:
    print("Remis!")
elif (player1 == '0' and player2 == '1') or (player1 == '1' and player2 == '2') or (player1 == '2' and player2 == '0'):
    print("Gracz 1 wygrywa!")
else:
    print("Gracz 2 wygrywa!")
