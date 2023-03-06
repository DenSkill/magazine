import pytest

from main.magazine import Item
from main.magazine import Phone


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
    item = Item('Смартфон', 10000, 20)
    with pytest.raises(Exception):
        item.name = 'СмартфонСмартифон'

def test_sim(): # тест количества сим-карт
    phone = Phone('Смартфон', 10000, 20, 1)
    with pytest.raises(Exception):
        phone.number_of_sim = 0