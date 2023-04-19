# using pytest
# pytest -v -s test_valid_positions.py
import pytest
from Algo import Algo

def test_valid_position1():
    position = (1, 1)
    assert Algo.isValidPosition(position) == True

def test_valid_position2():
    position = (1, 48)
    assert Algo.isValidPosition(position) == False

def test_valid_position3():
    position = (48, 0)
    assert Algo.isValidPosition(position) == False
    
def test_valid_position4():
    position = (-1, 0)
    assert Algo.isValidPosition(position) == False