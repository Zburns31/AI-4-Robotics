# -*- coding: utf-8 -*-
"""List comprehensions populating the grid in the video are written in a
somewhat confusing way, with row and col variables mixed up. The comprehension
 should be written as:

[[' ' for col in range(len(grid[0]))] for row in range(len(grid))]"""

# -----------
# User Instructions:
#
# Modify the the search function so that it becomes
# an A* search algorithm as defined in the previous
# lectures.
#
# Your function should return the expanded grid
# which shows, for each element, the count when
# it was expanded or -1 if the element was never expanded.
#
# If there is no path from init to goal,
# the function should return the string 'fail'
# ----------

grid = [
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0],
]
heuristic = [
    [9, 8, 7, 6, 5, 4],
    [8, 7, 6, 5, 4, 3],
    [7, 6, 5, 4, 3, 2],
    [6, 5, 4, 3, 2, 1],
    [5, 4, 3, 2, 1, 0],
]

init = [0, 0]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1

delta = [[-1, 0], [0, -1], [1, 0], [0, 1]]  # go up  # go left  # go down  # go right

delta_name = ["^", "<", "v", ">"]


def search(grid, init, goal, cost, heuristic):
    # ----------------------------------------
    # modify the code below
    # ----------------------------------------
    closed_list = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    closed_list[init[0]][init[1]] = 1

    expand = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]
    action = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]

    x = init[0]
    y = init[1]
    g = 0
    h = heuristic[x][y]
    f = g + h

    open_list = [[f, g, h, x, y]]  # Put f first so we can sort based on f values

    found = False  # flag that is set when search is complete
    resign = False  # flag set if we can't find expand
    count = 0

    while not found and not resign:
        if len(open_list) == 0:
            resign = True
            return "Fail"
        else:
            open_list.sort()
            open_list.reverse()
            next_node = open_list.pop()
            f = next_node[0]
            g = next_node[1]
            h = next_node[2]
            x = next_node[3]
            y = next_node[4]

            expand[x][y] = count
            count += 1

            if x == goal[0] and y == goal[1]:
                found = True
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if 0 <= x2 < len(grid) and 0 <= y2 < len(grid[0]):
                        if closed_list[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            h2 = heuristic[x2][y2]
                            f2 = g2 + h2
                            open_list.append([f2, g2, h2, x2, y2])
                            closed_list[x2][y2] = 1

    return expand


expand = search(grid, init, goal, cost, heuristic)

for i in range(len(expand)):
    print(expand[i])
