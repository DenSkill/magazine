import csv
import os
from os import fspath


class Item:
    pay_rate = 1.0
    all = []

    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count
        self.all.append(self)

    def __add__(self, other):
        if isinstance(other, Item):
            return int(self.count) + int(other.count)
        else:
            raise ValueError('Оба операнта должны принадлежать классу Item')

    def __repr__(self) -> str:
        return f'The object - Item, name - {self.__name},price - {self.price}, count - {self.count}'

    def __str__(self) -> str:
        return f'{self.__name}'

    def apply_discount(self):
        self.price = self.pay_rate * self.price

    def calculate_total_price(self):
        return (self.price * self.count)

    @staticmethod
    def is_int(data) -> bool:
        if float(data).is_integer():
            return True
        return False

    @classmethod
    def new_copy(cls) -> 'Item':
        """Создаёт новые экзэмпляры из csv файла"""
        copies = []
        with open(os.fspath(("items.csv")), 'r', encoding="UTF-8", newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                cls(row['name'], int(row['price']), int(row['quantity']))

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if len(name) <= 10:
            self.__name = name
        else:
            raise Exception('Длина наименования товара превышает 10 символов')

    def get_price(self):
        """Возвращает цену товра"""
        return self.price * self.count


class Phone(Item):
    def __init__(self, name, price, count, number_of_sim=1):
        super().__init__(name, price, count)
        if number_of_sim < 1:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        else:
            self.number_of_sim = number_of_sim

    def __repr__(self) -> str:
        return f'The object - Item, name - {self.name},price - {self.price}, count - {self.count}, sim_count - {self.number_of_sim}'

    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        if value < 1:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        else:
            self._number_of_sim = value


phone1 = Phone("iPhone 14", 120000, 5, 2)
keyboard = Item('qwe', 10, 1)
print(repr(phone1))
print(keyboard + phone1)
phone1.number_of_sim = 3
print(repr(phone1))
