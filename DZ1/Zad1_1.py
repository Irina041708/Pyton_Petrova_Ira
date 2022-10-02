# Напишите программу, которая принимает 
# на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

friday_day_num = int(input("Введите число от 1 до 7:   "))
if friday_day_num <= 5 and friday_day_num > 0:
    print (f"{friday_day_num} - рабочий день")
elif friday_day_num > 5 and friday_day_num <= 7:
    print (f"{friday_day_num} - выходной день")
else:
    print (f"Неверный ввод данных")