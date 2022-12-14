from openpyxl import load_workbook


def get_add_user_json(data_json: list) -> list:
    if not data_json:
        user: dict = {'Фамилия': input('Вводим - Фамилия: ')}
        user['Фамилия'] = user['Фамилия'].title()
    else:
        sample = data_json[0]
        user = {}
        for i in sample:
            user[i] = input(f'Введите {i}: ')
            if i == 'Фамилия':
                user[i] = user[i].title()
            else:
                user[i] = user[i].capitalize()
    data_json.append(user)
    return data_json


def get_add_save_user_xlsx(data_xlsx):
    wb = load_workbook("data_file.xlsx")
    data_xlsx = wb.active
    new_row1 = input("Введите фамилию: ")
    new_row2 = input("Введите имя: ")
    new_row3 = input("Введите год рождения: ")
    new_row4 = input("Введите телефон: ")
    data_xlsx.append([new_row1,new_row2,new_row3,new_row4])
    print(new_row1,new_row2,new_row3,new_row4)
    wb.save("data_file.xlsx")
    wb.close()
  