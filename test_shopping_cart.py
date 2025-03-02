import pytest
from shopping_cart import calculate_total, display_total

def test_calculate_total():
    # Тестовий кошик з товарами
    cart = [
        {'name': 'Item A', 'price': 10.99},
        {'name': 'Item B', 'price': 5.99}
    ]
    
    # Перевірка обчислення загальної суми
    assert calculate_total(cart) == 16.98

def test_calculate_total_with_empty_cart():
    # Перевірка обчислення загальної суми для порожнього кошика
    assert calculate_total([]) == 0

def test_display_total(capsys):
    # Перевірка виводу функції display_total
    display_total(25.47)
    captured = capsys.readouterr()
    assert captured.out == "Total price: $25.47\n"
