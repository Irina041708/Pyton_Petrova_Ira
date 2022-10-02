#Чтение данных из файла
path = 'file.txt'
date = open(path, 'r')
for line in date:
    print(line)
date.close()

# import N_Zad as N
# print(N.f(1))


# import N_Zad
# print(N_Zad.f(1))

exit()



user_number = ['----------------------------ddddddddddddddddddddt222222222222222222','y','red111111111111111']
date = open('file.txt', 'a')
date.writelines(user_number)  # Ещё дописываем, добавляем в наш файл
date.write('\n ПРИВЕТ \n')
date.close


user_number = ['t','y','red111111111111111']
date = open('file2.txt', 'a')
date.writelines(user_number)
date.close

