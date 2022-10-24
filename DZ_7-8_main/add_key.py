

def get_add_key(data):
    user = input('Введите название нового столбца: ')
    for x in data:
        x[user] = input(f'Введите значение: ')
    return data
