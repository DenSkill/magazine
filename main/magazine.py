import csv
import os
from os import fspath

from main.errors import InstantiateCSVError


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
    def instantiate_from_csv(cls, path: str):
        """"Считывает данные из csv-файла и создает экземпляры класса, инициализируя их данными из файла"""
        """Если файл не найден или поврежден выбрасывает соответствующие Exception"""

        if not os.path.isfile("../items.csv"):
            raise FileNotFoundError("отсутствует файл")
        try:
            with open(path, encoding='windows-1251') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if list(row.keys()) == ['name', 'price', 'quantity']:
                        cls(name=row['name'], price=float(row['price']), quantity=int(row['quantity']))
                    else:
                        raise InstantiateCSVError

        except KeyError:
            InstantiateCSVError('Файл items.csv поврежден')

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


class MixL:
    __language = "EN"

    @classmethod
    def change_lang(self):  # меняет язык
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"

    @property
    def language(self):
        return self.__language


class KeyBoard(Item, MixL):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__language = "EN"


