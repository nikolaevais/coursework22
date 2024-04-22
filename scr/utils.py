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