from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param.number_of_sim: количество слотов для SIM-карт,
        поддерживаемых телефоном.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.number_of_sim = number_of_sim

        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim


    def __add__(self, other):
        """добавление количества экземпляров телефона и товара"""
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise TypeError("Unsupported operand type(s) for +: 'Item' and '{}'".format(type(other).__name__))

    def __repr__(self) -> str:
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"