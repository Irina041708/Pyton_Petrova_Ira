# Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.


str1 = input("Введите первую строку:")
str2 = input("Введите вторую строку:")

count = 0

string = ''
subString = ''

if len(str1) > len(str2):
    string = str1
    subString = str2


else:
    string = str2
    subString = str1
    
print(string.count(subString))


# textFirst = input('Введите первую строку: ')
# textSecond = input('Введите вторую строку: ')



# string = ''
# subString = ''


# if len(textFirst) > len(textSecond):
#     string = textFirst
#     subString = textSecond
# else:
#     string = textSecond
#     subString = textFirst


# print(string.count(subString))

# count = 0
# counter = 0

# for i in range(len(string) - len(subString)):
#     if string[i] == subString[0]:
#         counterIn = 0
#         for k in range(len(subString)):
#             if subString[0+k] == string[i+k]:
#                 counterIn += 1
#         if counterIn == len(subString):
#             counter += 1

# print(f'Counter = {counter}')
