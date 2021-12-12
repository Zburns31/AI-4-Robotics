# -*- coding: utf-8 -*-
"""
The formula you need to use in the exercise is as follows. Note that it is a
little different from the ones in the video.

yi <- yi + alpha (xi - yi) + beta (yi + 1 + yi - 1 - 2 * yi)

There is an error in the solution presented in this video. newpath[i][j] is
updated two times in lines 37 and 38. This is incorrect: instead, newpath[i][j]
 should only be updated one time. An example fix would be to replace lines
 37-39 with the single update:

newpath[i][j] += weight_data * (path[i][j] - newpath[i][j]) +
                 weight_smooth * (newpath[i-1][j] + newpath[i+1][j] - 2.0 * newpath[i][j])

"""

# -----------
# User Instructions
#
# Define a function smooth that takes a path as its input
# (with optional parameters for weight_data, weight_smooth,
# and tolerance) and returns a smooth path. The first and
# last points should remain unchanged.
#
# Smoothing should be implemented by iteratively updating
# each entry in newpath until some desired level of accuracy
# is reached. The update should be done according to the
# gradient descent equations given in the instructor's note
# below (the equations given in the video are not quite
# correct).
# -----------

from copy import deepcopy

# thank you to EnTerr for posting this on our discussion forum
def printpaths(path, newpath):
    for old, new in zip(path, newpath):
        print(
            "["
            + ", ".join("%.3f" % x for x in old)
            + "] -> ["
            + ", ".join("%.3f" % x for x in new)
            + "]"
        )


# Don't modify path inside your function.
path = [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2], [3, 2], [4, 2], [4, 3], [4, 4]]


def smooth(path, weight_data=0.5, weight_smooth=0.1, tolerance=0.000001):

    # Make a deep copy of path into newpath
    newpath = deepcopy(path)

    #######################
    ### ENTER CODE HERE ###
    #######################
    change = tolerance
    # Loop until the value being changed is less than the tolerance value
    while change >= tolerance:
        change = 0.0
        for i in range(1, len(newpath) - 1):
            for j in range(len(newpath[0])):
                aux = newpath[i][j]
                newpath[i][j] += weight_data * (path[i][j] - newpath[i][j]) + weight_smooth * (
                    newpath[i - 1][j] + newpath[i + 1][j] - 2.0 * newpath[i][j]
                )
                change += abs(aux - newpath[i][j])

    return newpath  # Leave this line for the grader!


printpaths(path, smooth(path))
