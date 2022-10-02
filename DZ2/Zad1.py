# Напишите программу, которая принимает на вход вещественное число
#  и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11
float_num = float(input(f'Введите вещественное число:  '))
sum_ = 0
if float_num < 0:
    float_num *= -1
float_str = str(float_num)
for i in float_str:
    if i != '.':
        sum_ += int(i)
print(sum_)
