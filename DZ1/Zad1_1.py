# Напишите программу, которая принимает 
# на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

a = int(input("Введите число от 1 до 7:   "))
if a <= 5 and a > 0:
    print (f"{a} - рабочий день")
elif a > 5 and a <= 7:
    print (f"{a} - выходной день")
else:
    print (f"Неверный ввод данных")