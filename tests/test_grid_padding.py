# using pytest
# pytest -v -s test_grid_padding.py

import pytest
from Algo import Algo
import numpy as np

def test_grid_padding1():
    # get a grid of size 4x6
    grid = np.array([
        [1, 2, 3, 4, 5, 6],
        [7, 8, 9, 10, 11, 12],
        [13, 14, 15, 16, 17, 18],
        [19, 20, 21, 22, 23, 24]
    ])

    # get a padded grid of size 5x5
    padded_grid = Algo.padWithZeroIfOutOfBound(grid, (1, 1), 2, 2)

    expected_padded_grid = np.array([
        [0, 0, 0, 0, 0],
        [0, 1, 2, 3, 4],
        [0, 7, 8, 9, 10],
        [0, 13, 14, 15, 16],
        [0, 19, 20, 21, 22]
    ])

    assert padded_grid.shape == (5, 5)

    assert np.array_equal(padded_grid, expected_padded_grid)

def test_grid_padding2():
    # test to check padding in both sides
    grid = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]
    ])

    padded_grid = Algo.padWithZeroIfOutOfBound(grid, (3, 2), 3, 1)

    expected_padded_grid = np.array([
        [0, 7, 8, 9, 0, 0, 0],
        [0, 10, 11, 12, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ])

    assert expected_padded_grid.shape == (3, 7)

    assert np.array_equal(padded_grid, expected_padded_grid)

def test_grid_padding3():
    # mini check
    grid = np.array([[1]])

    padded_grid = Algo.padWithZeroIfOutOfBound(grid, (0, 0), 2, 2)

    expected_padded_grid = np.array([
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ])

    assert expected_padded_grid.shape == (5, 5)

    assert np.array_equal(padded_grid, expected_padded_grid)
    