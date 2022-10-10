# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (
# значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from numpy import poly1d, setbufsize
import numpy as np
np.linalg

degree_user = int(input("Введите степень: "))
result = poly1d( np.random.randint(0, 101, degree_user+1))
with open('Pyton_Ira_Petrova//DZ4//result_zad4.txt','w') as result_zad4:
    result_zad4.write(f"{result} = 0 ")
result_zad4.close() 
