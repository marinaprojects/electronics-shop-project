"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

data = Item("Смартфон", 10000, 20)


def test_calculate_total_price():
    """Проверяет правильность расчёта total_price"""
    assert data.calculate_total_price() == 200000
    assert data.quantity == 20


def test_apply_discount():
    """Проверяет правильность расчёта скидки на товар apply_discount"""
    data.pay_rate = 0.8
    data.apply_discount()
    assert data.price == 8000.0


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_instantiate_from_csv():
    Item.instantiate_from_csv()  # создание объектов из данных файла
    assert len(Item.all) == 5  # в файле 5 записей с данными по товарам
