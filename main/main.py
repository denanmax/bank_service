import json
from utils.load_data import read_data
from utils.functions import get_last_5_operations
from utils.functions import print_amount
from utils.functions import print_masked_accounts
from utils.functions import print_date_description

def main():
    """Читаем наш файл и выводим 5 последних операций"""
    try:
        data = read_data()
        for operation in get_last_5_operations(data):
            print_date_description(operation)
            print_masked_accounts(operation)
            print_amount(operation)
            print()

    except json.decoder.JSONDecodeError:
        print("Ошибка чтения данных из файла.")


if __name__ == "__main__":
    main()