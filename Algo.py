import heapq
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

class Algo:
    """
        This class contains the algorithm for finding a good enough trajectory from start to destination that minimizes collision with other agents.
    """
    @staticmethod
    def heuristic(pos1, pos2):
        """
        args:
            pos1: tuple of (x, y) coordinates
            pos2: tuple of (x, y) coordinates
            return: Euclidean distance between pos1 and pos2
        """
        return ((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)**0.5

    @staticmethod
    def find_good_enough_trajectory(start, destination, agent_trajectories, ruble_grid, factory_grid, max_time_steps=100):
        """
        run A* search to find a path from start to destination that minimizes collision with other agents
        args:
            start: tuple of (x, y) coordinates
            destination: tuple of (x, y) coordinates
            agent_trajectories: list of agent trajectories in the form of list of (x, y) coordinates
            ruble_grid: grid of ruble positions. an integer value indicating the cost of moving through the position
            factory_grid: grid of factory positions (x, y) coordinates. 0 if not a factory, 1 if a factory
            max_time_steps: maximum number of time steps to search for a path
            returns : a path from start to destination that minimizes collision with other agents, and the number of collisions
        """
    

        num_agents = len(agent_trajectories)
        max_time_steps = max(max(len(traj) for traj in agent_trajectories), max_time_steps)
        
        # get occupied positions for each time step
        occupiedPositions = Algo.getOccupiedPositionForTimeSteps(agent_trajectories, max_time_steps)


        # A* search
        # frontier is a priority queue of (heuristic + cost, cost, time, current, path)
        # cost is defined as the number of timesteps in which there was a colision
        # collision is found when an agent coexists in the same position as another agent
        # we use a priority queue to find the path with the lowest heuristic + cost
         
        frontier = [(Algo.heuristic(start, destination), 0, 0, start, [start])]

        # visited is a list of set of visited positions for each time step
        # initially it contains empty set for all time steps
        visited = [set() for _ in range(max_time_steps)]

        # add start to visited
        visited[0].add(start)

        # worst case runtime of while loop : O(max_time_steps * 48^2 * log(48^2))
        # python heap pop and push is O(log n)
        while frontier:
            # pop the item with the lowest heuristic + cost
            _, cost, time, current, path = heapq.heappop(frontier)

            print(f"Heuristic + cost = {_}, cost = {cost}")
            # found the destination
            if current == destination:
                return path, cost - time
            
            # if time is greater than max_time_steps, we have exceeded the maximum time steps
            # in this case, we ignore the path
            if time >= max_time_steps - 1:
                continue

            # increment time
            new_time = time + 1


            # trying to move in 4 directions
            print("Trying to move in 4 directions")
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_pos = (current[0] + dx, current[1] + dy)
                # check if new_pos is a valid position and not visited and not filled with factory
                if Algo.isValidPosition(new_pos) and new_pos not in visited[new_time] and not factory_grid[new_pos[0], new_pos[1]]:
                    print(f"Time: {new_time}, old_pos: {current} new_pos: {new_pos}, occupiedPositions: {occupiedPositions[new_time]}")
                    # add new_pos to visited
                    visited[new_time].add(new_pos)
                    # for each step taken, cost is linearly incremented
                    new_cost = cost + new_time
                    # if new_pos is occupied cost is heavily incremented
                    if new_pos in occupiedPositions[new_time]:
                        new_cost += 50000
                    # if new_pos is filled with ruble, cost is incremented by the ruble value
                    new_cost += ruble_grid[new_pos[0], new_pos[1]]

                    # add new_pos to path. runtime: O(1)
                    new_path = path + [new_pos]
                    new_frontier_item = (new_cost + Algo.heuristic(new_pos, destination), new_cost, new_time, new_pos, new_path)
                    
                    heapq.heappush(frontier, new_frontier_item)
        return None, None


    @staticmethod
    def getOccupiedPositionForTimeSteps(agent_trajectories, max_time_steps):
        """
        runtime: O(n * max_time_steps) where n is the number of agents
        we precompute the occupied positions for each time step and store them in a list of sets for faster lookup
        args: 
            agent_trajectories: list of agent trajectories in the form of list of (x, y) coordinates
            max_time_steps: maximum number of time steps to search for a path
            returns: list of set of occupied positions for each time step
        """
        num_agents = len(agent_trajectories)
        # max_time_steps = max(len(traj) for traj in agent_trajectories)
        occupied_positions = []

        # adding item to set is O(1)
        # i hope this is the right way to do it
        for t in range(max_time_steps):
            occupied_positions.append(set(agent_trajectories[i][t] for i in range(num_agents) if t < len(agent_trajectories[i])))
        return occupied_positions
    
    @staticmethod
    def isValidPosition(position):
        """
        args:
            position: tuple of (x, y) coordinates
            returns: True if position is a valid position in the grid
        """
        return position[0] >= 0 and position[0] < 48 and position[1] >= 0 and position[1] < 48
    
    @staticmethod
    def animate_trajectories(agentTrajectories, actorTrajectory):
        """
        args:
            agentTrajectories: list of agent trajectories in the form of list of (x, y) coordinates
            actorTrajectory: actor trajectory in the form of list of (x, y) coordinates
        returns:
            animation of the trajectories
        """
        # Define the grid size
        grid_size = 48

        # Create a figure and axis
        fig, ax = plt.subplots()
        ax.set_xlim(0, grid_size)
        ax.set_ylim(0, grid_size)


        # Define the scatter plot for the agents
        agents_scatter = ax.scatter([], [], color='black', s=50)


        # Define the line plot for the actor
        actor_line, = ax.plot([], [], color='red', linewidth=2)

        # Define the update function for the animation
        def update(frame):
            # Clear the axis
            ax.clear()

            # Set the axis limits
            ax.set_xlim(0, grid_size)
            ax.set_ylim(0, grid_size)

            # Set the axis ticks
            ax.set_xticks(np.arange(0, grid_size, 5))
            ax.set_yticks(np.arange(0, grid_size, 5))

            # Plot the actor trajectory
            actor_x, actor_y = zip(*actorTrajectory[:frame+1])
            actor_line.set_data(actor_x, actor_y)

            # Plot the agent trajectories
            for i, agent_trajectory in enumerate(agentTrajectories):
                if frame < len(agent_trajectory):
                    agent_x, agent_y = zip(*agent_trajectory[:frame+1])
                    ax.plot(agent_x, agent_y, color='black', linewidth=1)
                    ax.scatter(actor_x[-1], actor_y[-1], color='red', s=50)



            # Plot the agents as scatter points
            if frame < len(actorTrajectory):
                actor_x, actor_y = actorTrajectory[frame]
                agents_scatter.set_offsets(np.array([[actor_x, actor_y]]))
                ax.scatter(actor_x, actor_y, color='red', s=50)

            # Set the title
            ax.set_title('Frame {}'.format(frame))

        # Create the animation
        animation = FuncAnimation(fig, update, frames=len(actorTrajectory), interval=100)

        # Display the animation
        return HTML(animation.to_jshtml())
