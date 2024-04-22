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