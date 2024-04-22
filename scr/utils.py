import json
import datetime

def upload_file(filepath):
   '''
   Загружаем список операций из файла
   '''
   with open(filepath, encoding='utf-8') as file:
    operations = json.load(file)
    return operations


def sorting_information_by_parameter_state(file):
    '''
    Получаем список словарей,
    в которых state = EXECUTED
    '''
    operations = file
    list_state_executed = []
    for operation in operations:
        if operation.get('state') == "EXECUTED":
            list_state_executed.append(operation)
    return list_state_executed


def sort_by_transaction_date(file, n):
    '''
    сортировка по дате операции
    и сохранение пяти последних операции
    '''
    list_state_executed = file
    list_date_sort = sorted(list_state_executed, key=lambda x: x['date'], reverse=True)
    list_recent_transactions = list_date_sort[0:n]
    return list_recent_transactions


def change_date_format(file):
    '''
    изменение формата даты с ISO
    на DD.MM.YYYY
    '''
    list_change_date = []
    list_date = file
    for date in list_date:
        date_iso = datetime.datetime.fromisoformat(date['date'])
        list_change_date.append(date_iso.strftime("%d.%m.%Y"))
    return list_change_date


def change_from_format(file):
    '''
    изменение вида вывода номера карты
    или счета со звездочками
    '''
    list_change_card = []
    list_operation = file
    for item in list_operation:
        if item.get('from') == None:
            list_change_card.append("Нет данных")
        elif "Счет" in item.get('from'):
            list_change_card.append(f"Счет **{item['from'][-4:]}")
        else:
            card_new = ""
            card_number = item['from'].split()[-1]
            private_number = card_number[:6] + (len(card_number[6:-4]) * '*') + card_number[-4:]
            len_private_number, separation_private_number = len(private_number), len(private_number) // 4
            card_new += " ".join(item['from'].split()[:-1])
            card_new += " "
            card_new += " ".join([private_number[i:i + separation_private_number] for i in range(0, len_private_number, separation_private_number)])
            list_change_card.append(card_new)
    return list_change_card