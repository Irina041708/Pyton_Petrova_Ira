# Напишите программу, 
# которая по заданному номеру четверти,
#  показывает диапазон возможных координат точек в этой четверти (x и y).

numberQuarter = int(input("Введите номер четверти:  "))

if numberQuarter == 1:
    print(f"x > 0 и y > 0")
elif numberQuarter == 2:
    print(f"x < 0 и y > 0")
elif numberQuarter == 3:
    print(f"x < 0 и y < 0")
elif numberQuarter == 4:
    print(f"x > 0 и y < 0")