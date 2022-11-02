

def get_add_key(data_json):
    user = input('Введите название нового столбца: ')
    for x in data_json:
        x[user] = input(f'Введите значение: ')
    return data_json
