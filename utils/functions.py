from datetime import datetime

def get_last_5_operations(data):
    """Сортируем операции и получаем 5 последних"""
    executed_operations = []
    for operation in data:
        if "state" in operation and operation["state"] == "EXECUTED":
            executed_operations.append(operation)
    sorted_operations = sorted(executed_operations, key=lambda k: k['date'], reverse=True)
    return sorted_operations[:5]

def mask_account(account):
    """Маскируем ноиера счета/карты"""
    if not account:
        return ""

        # проверяем, что это номер карты
    if not "Счет" in account:
        result = account[:-12] + " " + account[-12:-10] + "** ****" + " " + account[-4:]
    else:
        result = "**" + account[-4:]

    return result

def convert_date(date_str):
    """Выставляем дату по нужному нам формату"""
    date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")

def print_operation(operation):
    """Собираем информацию из файла и функций и выводим на экран"""
    formatted_date = convert_date(operation["date"]) # дата нужного формата
    description = operation["description"] # описание операции
    try:
        from_account = operation["from"] # прорабатываем если "from" отсутствует
    except:
        from_account = ""
    to_account = operation["to"]
    amount = float(operation["operationAmount"]["amount"]) # сумма операции
    currency = operation["operationAmount"]["currency"]["name"] # валюта операции

    print(f"{formatted_date} {description}")
    print(f"{mask_account(from_account)} -> {mask_account(to_account)}")
    print(f"{amount} {currency}")
    print()



