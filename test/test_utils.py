import os.path
from config import ROOT_DIR

from scr.utils import upload_file
from scr.utils import change_from_format
from scr.utils import sorting_information_by_parameter_state
from scr.utils import change_date_format


for_test = [
    {"state": "EXECUTED", "date": "2018-07-15T18:44:13.346362", "from": "МИР 8665240839126074"},
    {"state": "CANCELED", "date": "2019-12-03T04:27:03.427014", "from": "Счет 18125798580985711166"},
    {"state": "EXECUTED", "date": "2019-02-14T17:38:09.910336"},
]
expected_result = [
    {"state": "EXECUTED", "date": "2018-07-15T18:44:13.346362", "from": "МИР 8665240839126074"},
    {"state": "EXECUTED", "date": "2019-02-14T17:38:09.910336"},
]

def test_utils_upload_file():
    DATA_FOR_TEST = os.path.join(ROOT_DIR, 'test', 'data_for_test.json')
    assert upload_file(DATA_FOR_TEST) == [1, 2, 3]

def test_utils_sorting_information_by_parameter_state():
    assert sorting_information_by_parameter_state(for_test) == expected_result

def test_utils_change_date_format():
    assert change_date_format(for_test) == ["15.07.2018", "03.12.2019", "14.02.2019"]

def test_utils_change_from_format():
    assert change_from_format(for_test) == ["МИР 8665 24** **** 6074", "Счет **1166", "Нет данных"]