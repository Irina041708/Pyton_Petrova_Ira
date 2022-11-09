import time
import json


def append_to_json(data_file, list):
    with open(data_file, 'a', encoding="UTF-8") as f:
        json.dump(list, f, ensure_ascii=False, indent=5)
    time.sleep(1)
    return
