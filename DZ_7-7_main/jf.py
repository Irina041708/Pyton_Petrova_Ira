import json


def read_file():
    with open("data_file.json", "r", encoding='utf8') as read_file:
        data_json = json.load(read_file)
    return data_json


def write_in_file(data_json):
    with open("data_file.json", "w", encoding='utf8') as write_file:
        json.dump(data_json, write_file, ensure_ascii=False, indent=5)
