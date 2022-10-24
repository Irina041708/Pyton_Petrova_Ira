

def get_conclusion(data):
    for i, item in enumerate(data):
        item_str = str(item).translate({ord(i): None for i in '{' '}' '\''})
        print(f'{i}. {item_str}')