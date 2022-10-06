# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list_usernumbers = [int(i) for i in input("Введите числа через пробел: ").split()]
list_composition = []
for i in range(0, len(list_usernumbers), 1):
    if i <= int((len(list_usernumbers)) / 2) and i <= int((len(list_usernumbers) - 1) / 2):
        list_composition.append(list_usernumbers[i]*list_usernumbers[len(list_usernumbers) - 1 - i])
print(f'{list_composition}')
