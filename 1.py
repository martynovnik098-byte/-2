a = float(input("Введите сторону a: "))
b = float(input("Введите сторону b: "))
c = float(input("Введите сторону c: "))
if a + b > c and a + c > b and b + c > a:
    p = (a + b + c) / 2
    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(f"Площадь треугольника: {S:.2f}")
else:
    print("Треугольник с такими сторонами не существует")
