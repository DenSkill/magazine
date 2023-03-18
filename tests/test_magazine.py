import pytest

from main.magazine import Item, KeyBoard
from main.magazine import Phone


def test_item_init():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000.0


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

def test_cls_keyboard():
    kb = KeyBoard('Dark', 9600, 5)
    assert str(kb) == 'Dark'
    assert str(kb.language) == 'EN'
    kb.change_lang()
    assert str(kb.language) == 'RU'