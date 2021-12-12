# -*- coding: utf-8 -*-
# -----------
# User Instructions:
#
# Modify the function search so that it returns
# a table of values called expand. This table
# will keep track of which step each node was
# expanded.
#
# Make sure that the initial cell in the grid
# you return has the value 0.
# ----------

grid = [
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 0],
]
init = [0, 0]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1

delta = [[-1, 0], [0, -1], [1, 0], [0, 1]]  # go up  # go left  # go down  # go right

delta_name = ["^", "<", "v", ">"]


def search(grid, init, goal, cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------
    g = 0
    x, y = init[0], init[1]
    open_vals = [[g, x, y]]
    count = 0

    expand = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]
    closed = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    closed[x][y] = 1

    found = False
    resign = False

    while not found and not resign:
        if len(open_vals) == 0:
            resign = True
            # print("Failed to find the goal cell")
            next_val = "fail"

        else:
            # remove node from the list
            open_vals.sort()  # sort list in ascending order by G value
            open_vals.reverse()  # Sort list in descending order with smallest G-value at the end
            next_val = open_vals.pop()  # Remove the smallest G value
            # print(f"Next Val: {next_val}")

            g, x, y = next_val

            expand[x][y] = count
            count += 1
            # for row in range(len(expand)):
            #     print(expand[row])

            # check if we are done
            if x == goal[0] and y == goal[1]:
                found = True
                print(next_val)

            else:
                for i in range(len(delta)):
                    # print(f"Action {delta[i]}")
                    # Check each action
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]

                    # Check to see if values fall within the grid
                    if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            # print(f"Next Position: {x2, y2}")
                            g2 = g + cost
                            open_vals.append([g2, x2, y2])
                            # print(f"Open vals {open_vals}")
                            closed[x2][y2] = 1

    return expand


search(grid, init, goal, cost)

##### Do Not Modify ######

import grader
from test import delta, delta_name

try:
    response = grader.run_grader(search)
    print(response)

except Exception as err:
    print(str(err))
