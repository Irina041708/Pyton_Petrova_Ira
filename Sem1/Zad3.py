# 1. Напишите программу, которая будет на вход принимать
#  число N и выводить числа от -N до N
# Примеры:
# 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5


a = int(input('Введите число'))
b = a *-1

if a < b+1:
    while a < b+1:
        print(f'{a}')
        a +=1

else:
    while b < a+1:
        print(f'{b}')
        b +=1


