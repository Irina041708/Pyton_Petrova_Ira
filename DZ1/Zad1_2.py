# Напишите программу, которая принимает 
# на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

friday_day_num = int(input("Введите число от 1 до 7:   "))
match friday_day_num:
    case 1:
        print(f"{friday_day_num} - рабочий день")
    case 2:
        print(f"{friday_day_num} - рабочий день")
    case 3:
        print(f"{friday_day_num} - рабочий день")
    case 4:
        print(f"{friday_day_num} - рабочий день")
    case 5:
        print(f"{friday_day_num} - рабочий день")
    case 6:
        print(f"{friday_day_num} - выходной день")
    case 7:
        print(f"{friday_day_num} - выходной день")
    case _:
        print(f"{friday_day_num} - ошибка ввода")
    