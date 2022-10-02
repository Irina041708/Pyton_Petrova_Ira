# Задайте список из n чисел последовательности 3n + 1 и выведите на экран их сумму.
# Пример:
#  Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

number = int(input("Введите число N: "))
list_number = {}
sum_list_number = 0
for key in range(1, number+1):
    list_number[key] = key*3+1
    sum_list_number += list_number[key]
print(f'N = {number} : {list_number} -> Cумма = {sum_list_number}')
