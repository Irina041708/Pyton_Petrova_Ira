# Напишите программу, которая принимает на вход число N и
# выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
from math import factorial
from turtle import begin_fill
number = int(input('Введите число: '))
result = []
result2 = []
count_result2 = 1
for i in range(1, number + 1):
    result.append(str(factorial(i)))
print(f"N = {number}, тогда", "[", ",".join(result), end=" ]  -> ")
for i in range(1, number + 1):
    count_result2 += 1
    print("(", "*".join([str(i) for i in range(1, count_result2)]), end=") ")
