print("Единицы: км, м, см, мм, mi, yd")
from_unit = input("Из какой единицы перевести? ")
to_unit = input("В какую единицу перевести? ")
value = float(input("Введите значение: "))
if from_unit == "км":
    meters = value * 1000
elif from_unit == "м":
    meters = value
elif from_unit == "см":
    meters = value * 0.01
elif from_unit == "мм":
    meters = value * 0.001
elif from_unit == "mi":
    meters = value * 1609.34
elif from_unit == "yd":
    meters = value * 0.9144
else:
    print("Неизвестная единица")
    exit()
if to_unit == "км":
    result = meters / 1000
elif to_unit == "м":
    result = meters
elif to_unit == "см":
    result = meters / 0.01
elif to_unit == "мм":
    result = meters / 0.001
elif to_unit == "mi":
    result = meters / 1609.34
elif to_unit == "yd":
    result = meters / 0.9144
else:
    print("Неизвестная единица")
    exit()
print(f"{value} {from_unit} = {result:.2f} {to_unit}")
