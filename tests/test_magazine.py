from main.magazine import Item
import csv
import pytest

def test_calculate_total_price():
    item3 = Item("Смартфон", 10000, 20)
    assert item3.calculate_total_price() == 200000

def test_name_length_10(): # тест длины названия
    item = Item('Смартфон',10000,20)
    item2 = Item('СССССССмартфон',10000,20)
    assert len(item.name) <= 10
    assert len(item2.name) > 10

def test_is_int():
    assert Item.is_int(5) == True
    assert Item.is_int(5.5) == False
