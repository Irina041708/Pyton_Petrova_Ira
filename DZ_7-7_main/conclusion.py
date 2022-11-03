

def get_conclusion_json(data_json):
    print(f'\n\nТелефонный справочник в фомате json: ')
    for i, items in enumerate(data_json):
        item_str = str(items).translate({ord(i): None for i in '{' '}' '\''})
        print(i,item_str)


def get_conclusion_xlsx_2(data_xlsx_2):
    print(f'\n\nТелефонный справочник в фомате xlsx: ')
    print(data_xlsx_2)
    return data_xlsx_2


def get_conclusion_xlsx(data_xlsx):
    print(f'\n\nТелефонный справочник в фомате xlsx: ')
    for row in range(1,data_xlsx.max_row+1):
        Фамилия = data_xlsx[row][0].value
        Имя = data_xlsx[row][1].value
        Возраст = data_xlsx[row][2].value
        Телефон = data_xlsx[row][3].value
        print(row, Фамилия, Имя, Возраст, Телефон)
    return data_xlsx
