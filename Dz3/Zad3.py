# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов.
# Пример:
# - [1.1 1.2 3.1 5 10.01] => 0.19

list_usernumbers = [float(i) for i in input("Введите числа через пробел: ").split()]
list = []
max_num = round(list_usernumbers[0] % 1, 3)
min_num = round(list_usernumbers[0] % 1, 3)
list = [num % 1 for num in list_usernumbers if num % 1 > 0.0001]
print(list)
print(max(list))
print(min(list))
print(round((max(list) - min(list)), 3))

