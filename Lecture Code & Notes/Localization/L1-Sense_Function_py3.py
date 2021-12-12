# -*- coding: utf-8 -*-
# Modify the code below so that the function sense, which
# takes p and Z as inputs, will output the NON-normalized
# probability distribution, q, after multiplying the entries
# in p by pHit or pMiss according to the color in the
# corresponding cell in world.


p = [0.2, 0.2, 0.2, 0.2, 0.2]
# p = [0, 1, 0, 0, 0]
world = ["green", "red", "red", "green", "green"]
# Z = "green"
measurements = ["red", "red"]
motions = [1, 1]
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1


# def sense(p, Z):
#     #
#     # ADD YOUR CODE HERE
#     # Measurement update function
#     q = [0] * len(p)

#     for idx, color in enumerate(world):
#         if color == Z:
#             q[idx] = p[idx] * pHit
#         else:
#             q[idx] = p[idx] * pMiss

#     total = sum(q)
#     q = [i / total for i in q]
#     return q


# def move(p, U):
#     """
#     Return the distribution q after the move. If u = 0, q == p, u == 1, values are shifted to the right
#     Args:
#         p: Prior distribution
#         U: Number of times to move to the right
#     """
#     # Shift a list: https://stackoverflow.com/questions/2150108/efficient-way-to-rotate-a-list-in-python
#     q = []
#     for i in range(len(p)):
#         # p[(i-U)] --> Shifts are values according to the appropriate direction
#         # If U = 1, then p[-1] becomes p[0]
#         prob = (
#             pExact * p[(i - U) % len(p)]
#             + pUndershoot * p[(i - U - 1) % len(p)]
#             + pOvershoot * p[(i - U + 1) % len(p)]
#         )
#         q.append(prob)

#     # Alternative solution
#     # U = U % len(p)
#     # q = p[-U:] + p[:-U]

#     return q


# for i in range(1000):
#     p = move(p, 1)


# def sense(p, Z):
#     "Alternate function implementation"

#     q = []
#     for i in range(len(p)):
#         hit = Z == world[i]
#         q.append(p[i] * (hit * pHit + (1 - hit) * pMiss))
#     return q

# for idx in range(len(measurements)):
#     p = sense(p, measurements[idx])
#     p = move(p, motions[idx])
#     print(p)

############################################################################################
# PS1 Code
############################################################################################

colors = [
    ["R", "G", "G", "R", "R"],
    ["R", "R", "G", "R", "R"],
    ["R", "R", "G", "G", "R"],
    ["R", "R", "R", "R", "R"],
]
measurements = ["G", "G", "G", "G", "G"]
motions = [[0, 0], [0, 1], [1, 0], [1, 0], [0, 1]]
sensor_right = 0.7
p_move = 0.8


def sense(p, measurement, colors, sensor_right):
    """
    """
    q = [[0 for col in range(len(p[0]))] for row in range(len(p))]
    sensor_wrong = 1.0 - sensor_right

    for row in range(len(colors)):
        for col in range(len(colors[row])):

            if measurement == colors[row][col]:
                q[row][col] = sensor_right * p[row][col]
            else:
                q[row][col] = sensor_wrong * p[row][col]

    total = sum([sum(lis) for lis in q])
    for row in range(len(q)):
        for col in range(len(q[row])):
            q[row][col] = q[row][col] / total

    return q


def move(p, motion, p_move):
    p_stay = 1.0 - p_move

    q = [[0 for col in range(len(p[0]))] for row in range(len(p))]

    # Iterate through each cell of p and compute the new probability of reaching that cell
    for i in range(len(p)):
        for j in range(len(p[i])):
            prob = (
                p_move * p[(i - motion[0]) % len(p)][(j - motion[1]) % len(p[i])]
                + p_stay * p[(i - motion[0]) % len(p)][(j - motion[1]) % len(p[i])]
            )
            q[i][j] = prob

    return q


def q4_localize(colors, measurements, motions, sensor_right, p_move):
    """
    Steps:
        1. Compute prior belief
        2. Move the robot
        3. Take a measurement and build the posterior distribution
    """
    # initializes p to a uniform distribution over a grid of the same dimensions as colors
    pinit = 1.0 / float(len(colors)) / float(len(colors[0]))
    p = [[pinit for _col in range(len(colors[0]))] for _row in range(len(colors))]

    # >>> Insert your code here <<<
    # print(p)

    # Create new grid with same dimensions as p
    # q = [[0 for col in range(len(p))] for row in range(len(p[0]))]

    # for row in range(len(q)):
    #     for col in range(len(q[row])):
    for i in range(len(motions)):
        p = move(p, motions[i], p_move)
        p = sense(p, measurements[i], colors, sensor_right)

    return p


post = q4_localize(colors, measurements, motions, sensor_right, p_move)
