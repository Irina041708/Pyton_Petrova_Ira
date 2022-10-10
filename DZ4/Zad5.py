# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

from numpy import poly1d, setbufsize
import numpy as np
np.linalg

polynomial1 = []
polynomial2 = []
file1 = open('Pyton_Ira_Petrova//DZ4//file1.txt', 'r')
file2 = open('Pyton_Ira_Petrova//DZ4//file2.txt', 'r')
line1 = file1.read()
line2 = file2.read()
file1.close()
file2.close()
for i in line1.split(): 
    polynomial1.append(int(i))
for j in line2.split():
    polynomial2.append(int(j))
result_polynomial = poly1d(np.polynomial.polynomial.polyadd(polynomial1,polynomial2))
with open('Pyton_Ira_Petrova//DZ4//result_zad5.txt','w') as result_zad5:
    result_zad5.write(f"{result_polynomial} = 0 ")
result_zad5.close()    
