from main.magazine import Item
import csv
import pytest


def test_new_copy():
    Item.new_copy()
    assert len(Item.all) == 5


def test_calculate_total_price():
    item3 = Item("Смартфон", 10000, 20)
    assert item3.calculate_total_price() == 200000


def test_is_int():
    item = Item('Смартфон', 10000, 20)
    assert item.is_int(5) == True
    assert item.is_int(5.5) == False


def test_name():  # тест длины названия
    item = Item('12345678910', 1, 1)
    if len(item.name) > 10:
        with pytest.raises(Exception):
            item.name = 'Длина наименования товара превышает 10 символов'