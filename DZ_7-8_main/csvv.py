import csv


def read_file():
    
    with open('Pyton_Ira_Petrova//DZ7_main//data_file.csv', encoding='utf-8') as r_file:
        # Создаем объект reader, указываем символ-разделитель ","
        file_reader = csv.reader(r_file, delimiter=",")
        # Считывание данных из CSV файла, формирование словаря
        data = csv.load(read_file)
    return data


def write_in_file(data):
    """
    Метод позволяет записать текст в файл file_name
    """
    with open('Pyton_Ira_Petrova//DZ7_main//data_file.csv', mode="w", encoding='utf-8') as w_file:
        names = ['Фамилия', 'Имя', 'Телефон', 'Описание']
        file_writer = csv.DictWriter(w_file, delimiter=',',
                                     lineterminator="\r", fieldnames=names)
        for i in data:
            file_writer.writerow(i)
