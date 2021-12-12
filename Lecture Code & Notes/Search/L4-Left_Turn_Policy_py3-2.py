# -*- coding: utf-8 -*-
"""
Creating new global variables (other than forward, forward_name, action, and
action_name) that you rely on in your function(s) may cause the grading script
to reject your submission.
"""

# ----------
# User Instructions:
#
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's
# optimal path to the position specified in goal;
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a
# right turn.

forward = [[-1, 0], [0, -1], [1, 0], [0, 1]]  # go up  # go left  # go down  # go right
forward_name = ["up", "left", "down", "right"]

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ["R", "#", "L"]

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space
grid = [
    [1, 1, 1, 0, 0, 0],
    [1, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 1],
]

init = [4, 3, 0]  # given in the form [row,col,direction]
# direction = 0: up
#             1: left
#             2: down
#             3: right

goal = [2, 0]  # given in the form [row,col]

cost = [2, 1, 20]  # cost has 3 values, corresponding to making
# a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------


def optimum_policy2D(grid, init, goal, cost):

    value = [
        [[999 for col in range(len(grid[0]))] for row in range(len(grid))],
        [[999 for col in range(len(grid[0]))] for row in range(len(grid))],
        [[999 for col in range(len(grid[0]))] for row in range(len(grid))],
        [[999 for col in range(len(grid[0]))] for row in range(len(grid))],
    ]

    policy = [
        [[" " for col in range(len(grid[0]))] for row in range(len(grid))],
        [[" " for col in range(len(grid[0]))] for row in range(len(grid))],
        [[" " for col in range(len(grid[0]))] for row in range(len(grid))],
        [[" " for col in range(len(grid[0]))] for row in range(len(grid))],
    ]

    policy2D = [[" " for col in range(len(grid[0]))] for row in range(len(grid))]

    change = True
    while change:
        change = False

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                for orientation in range(4):
                    # Walk through and look for the goal state. Once we find it, set its value to 0 so we can recursively walk backwards finding the optimal path
                    # print(f"checking Row {row}, column {col}")
                    if goal[0] == row and goal[1] == col:
                        if value[orientation][row][col] > 0:
                            value[orientation][row][col] = 0
                            policy[orientation][row][col] = "*"
                            # for i in range(len(value)):
                            #     print(value[i])
                            # print("Goal state found")
                            change = True

                    elif grid[row][col] == 0:
                        # Calculate the three ways to propogate the value
                        for i in range(3):
                            o2 = (orientation + action[i]) % 4
                            row2 = row + forward[o2][0]
                            col2 = col + forward[o2][1]

                            # Check whether values are within bounds
                            if (
                                row2 >= 0
                                and row2 < len(grid)
                                and col2 >= 0
                                and col2 < len(grid[0])
                                and grid[row2][col2] == 0
                            ):
                                new_value = value[o2][row2][col2] + cost[i]
                                if new_value < value[orientation][row][col]:
                                    value[orientation][row][col] = new_value
                                    policy[orientation][row][col] = action_name[i]
                                    change = True
    x = init[0]
    y = init[1]
    orientation = init[2]

    policy2D[x][y] = policy[orientation][x][y]
    while policy[orientation][x][y] != "*":
        if policy[orientation][x][y] == "#":
            o2 = orientation
        elif policy[orientation][x][y] == "R":
            o2 = (orientation - 1) % 4
        elif policy[orientation][x][y] == "L":
            o2 = (orientation + 1) % 4
        x = x + forward[o2][0]
        y = y + forward[o2][1]
        orientation = o2
        policy2D[x][y] = policy[orientation][x][y]

    for i in range(len(policy2D)):
        print(policy2D[i])

    return policy2D


optimum_policy2D(grid, init, goal, cost)
