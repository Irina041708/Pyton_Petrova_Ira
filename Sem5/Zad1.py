# В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
#  Найдите это число.


numbers = []
date = open('Pyton_Ira_Petrova//Sem5//file.txt', 'r')
line = date.read()
date.close()
print(line)

for i in line.split():
    numbers.append(int(i))
for i in range(1,len(numbers)):
    if not numbers[i-1] != numbers[i] - 1:
        continue
    else:
        print(f"Пропущенное число равно {numbers[i]-1}")


# numbers = []
# path = 'file.txt'
# date = open(path, 'r')
# line = date.read()
# date.close()
# print(line)
    
# for i in line.split(): 
#     numbers.append(int(i))
# print(numbers)
# count = numbers[0]
# for i in range(1, len(numbers)):
#     count += 1
#     # if numbers[i - 1] == numbers[i] - 1:
#     if numbers[i] == count:
#         continue
#     else:
#         print(f"Числа нет {count}")
