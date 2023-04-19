# using pytest
# pytest -v -s test_trajectory.py

import pytest 
from Algo import Algo
import logging

logging.basicConfig(level=logging.INFO)

# @pytest.mark.xfail
def test_trajectory1():
    start = (1, 1)
    destination = (1, 10)
    # we start with a small trajectory (max 4 timesteps) of 3 agents
    agent_trajectories = [
        [(5, 3), (5, 4), (5, 5), (5, 6)],
        [(2, 1), (2, 2), (2, 3), (2, 4)],
        [(3, 4), (3, 5), (3, 6), (3, 7)]
    ]

    agent_trajectory, collision = Algo.find_good_enough_trajectory(start, destination, agent_trajectories)
    # we log the agent_trajectory and collision
    logging.info("agent_trajectory: %s", agent_trajectory)
    logging.info("collision: %s", collision)

    assert False


def test_trajectory2():
    assert True