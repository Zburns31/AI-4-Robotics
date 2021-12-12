# -*- coding: utf-8 -*-
# ----------
# User Instructions:
#
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space


grid = [
    [0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 0],
]
init = [0, 0]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1

delta = [[-1, 0], [0, -1], [1, 0], [0, 1]]  # go up  # go left  # go down  # go right

delta_name = ["^", "<", "v", ">"]


def search(grid, init, goal, cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    g = 0
    x, y = init[0], init[1]
    open_vals = [[g, x, y]]

    closed = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    closed[x][y] = 1

    found = False
    resign = False

    while not found and not resign:
        if len(open_vals) == 0:
            resign = True
            print("Failed to find the goal cell")
            next_val = "fail"

        else:
            # remove node from the list
            open_vals.sort()  # sort list in ascending order by G value
            open_vals.reverse()  # Sort list in descending order with smallest G-value at the end
            next_val = open_vals.pop()  # Remove the smallest G value

            g, x, y = next_val

            # check if we are done
            if x == goal[0] and y == goal[1]:
                found = True
                print(next_val)

            else:
                for i in range(len(delta)):
                    # Check each action
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]

                    # Check to see if values fall within the grid
                    if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            open_vals.append([g2, x2, y2])
                            closed[x2][y2] = 1

    return next_val


# search(grid, init, goal, cost)

##### Do Not Modify ######

import first_search_grader

try:
    response = first_search_grader.run_grader(search)
    print(response)

except Exception as err:
    print(str(err))
