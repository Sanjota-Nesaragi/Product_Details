import pytest
from product import product_info

def test_product_info():
    expected_output = "Product ID: 101,\n Name: Keyboard,\n Quantity: 5,\n Price: 499.99\n"
    
    assert product_info(101, "Keyboard", 5, 499.99) == expected_output
