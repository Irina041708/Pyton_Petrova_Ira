# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# *Пример:*
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1
string_a = input('Введите строку: ')
a = ['привет','пока','домой','хай','пока','домой','мобилизация']
count = 0
count_index = 0
for i in a:
    if i == string_a:
        count += 1
        if count == 2:
            print(count_index)
            exit()
    count_index += 1
print('-1')
