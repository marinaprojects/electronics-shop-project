import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    DATA_DIR = '../src/items.csv'
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        price = self.price * self.quantity
        return price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        """добавить геттер"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """добавить сеттер
        длина наименования товара не больше 10 симвовов"""
        self.__name = value[:10]

    @classmethod
    def instantiate_from_csv(cls):
        """класс-метод, инициализирующий экземпляры класса
        `Item` данными из файла _src/items.csv_"""
        with open(cls.DATA_DIR, newline='', encoding='windows-1251') as csvfile:
            reader = csv.DictReader(csvfile)
            cls.all.clear()
            for row in reader:
                #print(row['name'], row['price'], row['quantity'])
                name = row['name']
                price = row['price']
                quantity = row['quantity']
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(param):
        """статический метод, возвращающий число из числа-строки"""
        return int(float(param))

