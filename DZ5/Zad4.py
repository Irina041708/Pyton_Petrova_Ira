# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

from collections import Counter

list_num = []
with open('Pyton_Ira_Petrova//DZ5//inut_zad4.txt','r') as inut:
    list = inut.read()
    inut.close()   
for i in list.split(): 
    list_num.append(int(i))
counts = Counter(list_num)
with open('Pyton_Ira_Petrova//DZ5//compression_zad4.txt','w') as compression_output:
    compression_output.write(f"{counts}")
compression_output.close() 
recovery = sorted(counts.elements())
with open('Pyton_Ira_Petrova//DZ5//recovery_zad4.txt','w') as recovery_output:
    recovery_output.write(f"{recovery}")
recovery_output.close() 

