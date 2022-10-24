
def get_add_user(data: list) -> list:
    if not data:
        user: dict = {}
        user['Фамилия'] = input('Вводим - Фамилия: ')
        user['Фамилия'] = user['Фамилия'].title()
    else:
        sample = data[0]
        user = {}
        for i in sample:
            user[i] = input(f'Введите {i}: ')
            if i == 'Фамилия':
                user[i] = user[i].title()
            else:
                user[i] = user[i].capitalize()
    data.append(user)
    return data