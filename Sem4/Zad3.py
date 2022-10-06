def find(a, b):    
    if a > b:
        max_num = a
        min_num = b
    else:
        max_num = b
        min_num = a
    for i in range(2, min_num):
        if min_num % i == 0 and max_num % i == 0:
            return i        


a = int(input("Введите число а: "))
b = int(input("Введите число b: "))
nok = find(a, b)
print(nok)
