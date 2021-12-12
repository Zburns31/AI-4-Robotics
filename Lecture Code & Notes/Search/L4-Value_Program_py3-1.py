# -*- coding: utf-8 -*-
# ----------
# User Instructions:
#
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal.
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0],
]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1  # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0], [0, -1], [1, 0], [0, 1]]  # go up  # go left  # go down  # go right

delta_name = ["^", "<", "v", ">"]


def compute_value(grid, goal, cost):
    """ Function that implements dynamic programming to find the best possible action
    from any cell in the grid. We make use of a policy and value data structure to
    track our movements through time

    This function first finds the goal cell, and works backwards computing the 'value' of each cell there
    after, moving its way towards the starting point

    """

    value = [[99 for col in range(len(grid[0]))] for row in range(len(grid))]
    policy = [[" " for col in range(len(grid[0]))] for row in range(len(grid))]

    # While we keep updating our intenal state, keep looping through trying to find the best path
    change = True
    while change:
        change = False

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # Walk through and look for the goal state. Once we find it, set its value to 0 so we can
                # recursively walk backwards finding the optimal path

                if goal[0] == row and goal[1] == col:
                    if value[row][col] > 0:
                        value[row][col] = 0
                        policy[row][col] = "*"
                        # for i in range(len(value)):
                        #     print(value[i])
                        print("Goal state found")
                        change = True

                # Check each cell as we iterate through and compute the value of that cell to the goal state
                elif grid[row][col] == 0:
                    print(f"Original Row/Column {row, col} with value {value[row][col]}")
                    for action in range(len(delta)):
                        row2 = row + delta[action][0]
                        col2 = col + delta[action][1]

                        # Check whether values are within bounds
                        if (
                            row2 >= 0
                            and row2 < len(grid)
                            and col2 >= 0
                            and col2 < len(grid[0])
                            and grid[row2][col2] == 0
                        ):
                            new_value = value[row2][col2] + cost
                            print(
                                f"New Row/Column {row2, col2} with current value {value[row2][col2]} and new value {new_value}"
                            )
                            # print(f"New computed value is {new_value}")

                            if new_value < value[row][col]:
                                change = True
                                print(
                                    f"New value found: Cell {row} {col} has current value {value[row][col]} and now its {new_value}"
                                )
                                value[row][col] = new_value
                                policy[row][col] = delta_name[action]
                                # for i in range(len(value)):
                                #     print(value[i])
    for i in range(len(policy)):
        print(policy[i])

    # make sure your function returns a grid of values as
    # demonstrated in the previous video.
    return value


compute_value(grid, goal, cost)
