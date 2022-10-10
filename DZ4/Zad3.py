# Задайте последовательность чисел.
#  Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.

from collections import Counter

nums_user = [int(i) for i in input("Введите числа через пробел: ").split()]
counts = Counter(nums_user)
print([i for i in counts if counts[i] == 1])
