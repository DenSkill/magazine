import csv


class Item:
    pay_rate = 1.0
    all = []

    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count
        self.all.append(self)

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
        with open('items.csv', 'r', encoding="UTF-8", newline='') as csvfile:
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
