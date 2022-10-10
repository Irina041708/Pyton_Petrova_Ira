# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

# num = float(input("Введите натурально число:  "))

def numbers(n):
   i = 2
   list_num = []
   while i * i <= n:
       while n % i == 0:
           list_num.append(i)
           n = n / i
       i = i + 1
   if n > 1:
       list_num.append(int(n))
   return list_num
n = int(input('Введите число: '))
print(numbers(n))
