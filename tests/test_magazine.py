from main.magazine import Item
import pytest

def test_calculate_total_price():
    item3 = Item("Смартфон", 10000, 20)
    assert item3.calculate_total_price() == 200000
