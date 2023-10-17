import math
diameter = float(input("Введіть діаметр кола: "))
choice = input("Оберіть, що потрібно обчислити (площу - 'S', периметр - 'P'): ")
if choice == "S":
    radius = diameter / 2
    area = math.pi * (radius ** 2)
    print(f"Площа кола з діаметром {diameter} одиниць: {area} квадратних одиниць")
elif choice == "P":
    radius = diameter / 2
    perimeter = 2 * math.pi * radius
    print(f"Периметр кола з діаметром {diameter} одиниць: {perimeter} одиниць")
else:
    print("Ви ввели невірний вибір. Оберіть 'S' для площі або 'P' для периметру.")
