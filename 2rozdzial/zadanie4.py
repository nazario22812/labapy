import math

a = float(input("a> "))
b = float(input("b> "))
c = float(input("c> "))

delta = b**2 - 4*a*c

print(f"delta rowna sie = {delta}")

if delta < 0:
    print("pierwiastków")

elif delta == 0:
    x0 = -b/(2*a)
    print(f"x = {x0}")

elif delta >0:
    x1 = (-b + math.sqrt(delta))/(2*a)

    x2 = (-b - math.sqrt(delta))/(2*a)

    print(f"x1 = {x1}\nx2 = {x2}")