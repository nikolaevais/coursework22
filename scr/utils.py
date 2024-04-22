import json
import datetime

def upload_file(filepath):
   '''
   Загружаем список операций из файла
   '''
   with open(filepath, encoding='utf-8') as file:
    operations = json.load(file)
    return operations

