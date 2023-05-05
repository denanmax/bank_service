import pytest
import utils.functions



def test_get_last_5_operations():
    assert utils.functions.get_last_5_operations([]) == []
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
