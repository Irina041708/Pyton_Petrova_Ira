# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# с помощью математических формул нахождения корней квадратного уравнения
# с помощью дополнительных библиотек Python (например, numpy.roots)

import math
import numpy

a = int(input("Введите число: "))
b = int(input("Введите число: "))
c = int(input("Введите число: "))

# d = sqrt(b**2-4*a*c)
# if d < 0:
#     print("Нет корней")
# elif d == 0:
#     print(f'{-b/(2*a)}')
# else:
#     print(f'корень 1 -> {(-b+math.sqrt(d))/(2*a)}, корень 2 -> {(-b-math.sqrt(d))/(2*a)}')

p = [a, b, c]
print(f'{numpy.roots(p)}')
