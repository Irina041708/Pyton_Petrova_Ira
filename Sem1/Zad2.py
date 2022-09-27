# Напишите программу, которая на вход принимает 5 чисел
#  и находит максимальное из них.
# Примеры:
# 1. 1, 4, 8, 7, 5 -> 8
# 78, 55, 36, 90, 2 -> 90
# [78,55,36,90,2]

numbers = [78, 55, 36, 90, 2]
a = numbers[0]
for i in numbers:
    if a < i:
        a = i
print(a)



# a = int(input('Введите первое число '))
# b = int(input('Введите второго число '))
# c = int(input('Введите третье число '))
# d = int(input('Введите четвертое число '))
# e = int(input('Введите пятое число '))
# max_number = a
# if  max_number < b:
#     max_number = b
# if  max_number < c:
#     max_number = c
# if  max_number < d:
#     max_number = d
# if  max_number < e:
#     max_number = e
    
# print(f'Максимальное число {max_number}')




# my_list = [4, 5, 32, 9, 10]
# max_number = my_list[0]
# i = 0
# while i < len(my_list):
#    if max_number < my_list[i]:
#        max_number = my_list[i]     
#    i += 1

# print(f'{max_number}')

