import os
from config import ROOT_DIR

from utils import upload_file
from utils import sorting_information_by_parameter_state
from utils import sort_by_transaction_date
from utils import change_from_format
from utils import change_date_format

FILE_PATH = os.path.join(ROOT_DIR, 'data', 'operations.json')

def information_output():
    operations = upload_file(FILE_PATH)
    operation = sorting_information_by_parameter_state(operations)
    list_operation = sort_by_transaction_date(operation, 5)
    card = change_from_format(list_operation)
    date = change_date_format(list_operation)
    n = 0
    for item in list_operation:
        print(f"""{date[n]} {item['description']}
{card[n]} -> Счет **{item['to'][-4:]}
{item['operationAmount']['amount']} {item['operationAmount']['currency']['name']}
""")
        n += 1

print(information_output())
