# using pytest
# pytest -v -s test_occupied_positions.py

import pytest
from Algo import Algo

def test_occupied_position1():
    agent_trajectories = [
        [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10)],
        [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10)],
        [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10)]
    ]
    occupiedPositions = Algo.getOccupiedPositionForTimeSteps(agent_trajectories, 10)
    assert occupiedPositions == [
         {(1, 1)}, {(1, 2)}, {(1, 3)}, {(1, 4)}, {(1, 5)}, {(1, 6)}, {(1, 7)}, {(1, 8)}, {(1, 9)}, {(1, 10)}
    ]

def test_occupied_position2():
    agent_trajectories = [
        [(1, 1), (1, 2), (1, 3)],
        [(4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (4, 10)],
        [(20, 1), (20, 2)],
        [(6, 1), (6, 2), (6, 3), (6, 4)]
    ]
    occupiedPositions = Algo.getOccupiedPositionForTimeSteps(agent_trajectories , 6)
    assert occupiedPositions == [
        {(1, 1), (4, 5), (20, 1), (6, 1)}, {(1, 2), (4, 6), (20, 2), (6, 2)}, {(1, 3), (4, 7), (6, 3)}, {(4, 8), (6, 4)}, {(4, 9)}, {(4, 10)}
    ]

def test_occupied_position3():
    # when there is only one timestep per agent
    agent_trajectories = [
        [(1, 1)], [(4, 5)], [(20, 1)], [(6, 1)]
    ]
    occupiedPositions = Algo.getOccupiedPositionForTimeSteps(agent_trajectories, 3)
    assert occupiedPositions == [
        {(1, 1), (4, 5), (20, 1), (6, 1)}, set(), set()
    ]