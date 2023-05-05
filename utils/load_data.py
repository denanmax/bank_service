import json
def read_data():
    """Загружаем файл operations.json"""
    with open("../operations/operations.json", encoding='utf=8') as f:
        data = json.load(f)
    return data
