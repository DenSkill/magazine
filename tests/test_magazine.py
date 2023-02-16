import pytest
from main import Item

item3 = Item("Смартфон", 10000, 20)

def test_apply_discount(item3):
    assert item3.apply_discount() == 8000.0

def test_calculate_total_price():
    assert item3.calculate_total_price(1000, 20) == 20000
