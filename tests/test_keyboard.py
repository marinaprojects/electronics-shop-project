import pytest

from src.keyboard import Keyboard

kb = Keyboard('Dark Project KD87A', 9600, 5)


def test_initial_language():
    """проверяют начальную раскладку клавиатуры"""
    assert str(kb.language) == 'EN'

def test_change_language():
    """тесты для проверки правильной работы метода смены знака"""
    kb.change_lang()
    assert str(kb.language) == 'RU'
    kb.change_lang()
    assert str(kb.language) == 'EN'

def test_invalid_language_assignment():
    with pytest.raises(AttributeError):
        kb.language = 'CH'
