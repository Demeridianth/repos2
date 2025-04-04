import sys
import os

# Add the parent directory to sys.path so Python can find main.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from io import StringIO
from contextlib import redirect_stdout
from main import CoffeShop  # Replace 'your_module' with the actual module name

def test_make_coffee():
    shop = CoffeShop("Python Coffee")
    
    # Capture printed output
    f = StringIO()
    with redirect_stdout(f):
        shop.make_cofee(1, 2, 3)  # Medium black coffee with vanilla
    output = f.getvalue().strip()
    
    assert output == "your order is medium black with vanilla"

def test_invalid_coffee():
    shop = CoffeShop("Python Coffee")
    
    f = StringIO()
    with redirect_stdout(f):
        shop.make_cofee(99, 99, 99)  # Invalid inputs
    output = f.getvalue().strip()
    
    assert output == "your order is None None with None"


def test_no_extra():
    shop = CoffeShop('Python Coffee')

    string = StringIO()
    with redirect_stdout(string):
        shop.make_cofee(1, 2, 0)
    output = string.getvalue().strip()

    assert output == 'your order is medium black with None'
