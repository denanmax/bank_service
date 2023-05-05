from utils.functions import convert_date
from utils.functions import mask_account
def print_date_description(operation):
    """Собираем вместе дату и описание платежа"""
    print(f"{convert_date(operation['date'])} {operation['description']}")

def print_masked_accounts(operation):
    """Формируем скрыте данные карты/счета"""
    try:
        from_account = operation["from"] # прорабатываем если "from" отсутствует
    except:
        from_account = ""
    to_account = operation["to"]
    print(f"{mask_account(from_account)} -> {mask_account(to_account)}")

def print_amount(operation):
    """Формируем сумму и валюту платежа"""
    print(f"{float(operation['operationAmount']['amount'])} {operation['operationAmount']['currency']['name']}")