# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Пример: Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

Number = int(input("Введите число N:"))
# sumN = 1
# count = 0
# while count <= Number:
#     count += 1
#     sumN = 3*count+1
    
#     print(sumN)
result = {}
for key in range(1,Number+1):
    result[key] = key*3+1
print(result)
