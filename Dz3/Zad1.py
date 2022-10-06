# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

list_number = [int(i) for i in input("Введите числа через пробел: ").split()]
list_number2 = []
sum_number = 0
for i in range(1, len(list_number), 2):
    list_number2.append(list_number[i])
    sum_number = list_number[i] + list_number[i]
print(f'Из списка {list_number}-> на нечетных позициях стоят элементы {list_number2}. Их сумма равна {sum_number}')
