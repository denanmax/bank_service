import json
import os.path


def read_data(path):
    """Загружаем файл operations.json"""
    if not os.path.exists(path):
        return None

    with open("../operations/operations.json", encoding='utf=8') as f:
        data = json.load(f)
    return data
