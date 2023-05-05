import pytest
import utils.functions

def test_get_last_5_operations():
    assert utils.functions.get_last_5_operations([{}]) == []
    assert utils.functions.get_last_5_operations([{"state": "EXECUTED", "date": "2022-01-01"}]) == [{"state": "EXECUTED", "date": "2022-01-01"}]
    data = [
    {"state": "CANCELLED", "date": "2021-12-31"},
    {"state": "CANCELLED", "date": "2022-01-01"},
    {"state": "EXECUTED", "date": "2022-01-02"}
]
    assert utils.functions.get_last_5_operations(data) == [{"state": "EXECUTED", "date": "2022-01-02"}]
    data = [
        {"state": "EXECUTED", "date": "2022-01-01"},
        {"state": "EXECUTED", "date": "2022-01-02"},
        {"state": "CANCELLED", "date": "2022-01-03"},
        {"state": "EXECUTED", "date": "2022-01-04"},
        {"state": "EXECUTED", "date": "2022-01-05"},
        {"state": "EXECUTED", "date": "2022-01-06"},
        {"state": "EXECUTED", "date": "2022-01-07"}
    ]

    assert utils.functions.get_last_5_operations(data) == [
        {"state": "EXECUTED", "date": "2022-01-07"},
        {"state": "EXECUTED", "date": "2022-01-06"},
        {"state": "EXECUTED", "date": "2022-01-05"},
        {"state": "EXECUTED", "date": "2022-01-04"},
        {"state": "EXECUTED", "date": "2022-01-02"}
    ]

def test_mask_account():
    assert utils.functions.mask_account("Счет: 1234567890") == "Счет: **7890"
    assert utils.functions.mask_account("МИР 8201420097886664") == "МИР 8201 42** **** 6664"
    assert utils.functions.mask_account("") == ""
    assert utils.functions.mask_account("Счет 35116633516390079956") == "Счет: **9956"
    assert utils.functions.mask_account("Visa Gold 6527183396477720") == "Visa Gold 6527 18** **** 7720"


def test_convert_date():
    assert utils.functions.convert_date("2022-04-01T12:30:00.000000") == "01.04.2022"
    assert utils.functions.convert_date("2023-02-14T09:15:30.000000") == "14.02.2023"

def test_convert_date_value_error():
    with pytest.raises(ValueError):
        utils.functions.convert_date("2021-11-30T16:30:00")
    with pytest.raises(ValueError):
        utils.functions.convert_date("")

