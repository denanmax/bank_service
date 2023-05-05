import json
from utils.load_data import read_data
from utils.functions import get_last_5_operations
from utils.functions import print_operation
def main():
    """Читаем наш файл и выводим 5 последних операций"""
    try:
        data = read_data()
        for operation in get_last_5_operations(data):
            print_operation(operation)
    except json.decoder.JSONDecodeError:
        print("Ошибка чтения данных из файла.")


if __name__ == "__main__":
    main()