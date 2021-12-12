######################################################################
# This file copyright the Georgia Institute of Technology
#
# Permission is given to students to use or modify this file (only)
# to work on their assignments.
#
# You may NOT publish this file or make it available to others not in
# the course.
#
######################################################################

######################################################################
# How to use:
#
#   For fill-in questions, change the value of each answer variable.
#
#   For programming questions, change the implementation of the
#   function provided.
#
#   Run the file from the command line to check:
#
#       python ps3_answers.py
#
######################################################################

from __future__ import division
from builtins import str
from builtins import range
from builtins import object
from past.utils import old_div
import hashlib
from math import *
import random

# If you see different scores locally and on Gradescope this may be an indication
# that you are uploading a different file than the one you are executing locally.
# If this local ID doesn't match the ID on Gradescope then you uploaded a different file.
OUTPUT_UNIQUE_FILE_ID = False
if OUTPUT_UNIQUE_FILE_ID:
    import hashlib, pathlib

    file_hash = hashlib.md5(pathlib.Path(__file__).read_bytes()).hexdigest()
    print(f"Unique file ID: {file_hash}")

seed = 0  # This seed results in successful results for both numpy and python's rng
random.seed(seed)

# Note, the following import is not required, but you may uncomment it
# if you want to use numpy as part of your solution
# make sure to use the provided seed as well, this seed has been tested
# and allows a correct solution to pass the provided test cases:
# import numpy as np
# np.random.seed(seed)

# STUDENT ID

# Please specify your GT login ID in the whoami variable (ex: jsmith321).

whoami = "zburns6"

# QUESTION 1

# What is the probability that zero particles are in state A?

q1_n_1 = 0.75
q1_n_4 = 0.316  # round your answer to 3 decimal places
q1_n_10 = 0.0563  # round your answer to 4 decimal places

# QUESTION 2

q2_1_step_A = 3
q2_1_step_B = 3
q2_1_step_C = 3
q2_1_step_D = 3
q2_infinite_step_A = 3
q2_infinite_step_B = 3
q2_infinite_step_C = 3
q2_infinite_step_D = 3

# QUESTION 3

# Put 0 for unchecked, 1 for checked

q3_works_fine = 0
q3_ignores_robot_measurements = 1
q3_ignores_robot_motion = 0
q3_it_likely_fails = 1
q3_none_of_above = 0

# QUESTION 4


def q4_move(self, motion):
    # You can replace the INSIDE of this function with the move function you modified in the module quiz
    myrobot = robot()

    # Copy instance attributes to new object
    myrobot.length = self.length
    myrobot.orientation = self.orientation
    myrobot.bearing_noise = self.bearing_noise
    myrobot.distance_noise = self.distance_noise
    myrobot.steering_noise = self.steering_noise

    # Set noise for steering and distance
    new_steering = random.gauss(motion[0], self.steering_noise)
    new_distance = random.gauss(motion[1], self.distance_noise)

    # Calculate the turning angle
    beta = (tan(new_steering) * new_distance) / myrobot.length

    # code referenced from https://gatech.instructure.com/courses/192324/pages/4-circular-motion-answer?module_item_id=1634086
    # Check to see if beta is really small (I.e. basically completely straight forward motion)
    if abs(beta) < 0.001:
        myrobot.x = self.x + (new_distance * cos(self.orientation))
        myrobot.y = self.y + (new_distance * sin(self.orientation))
        myrobot.orientation = (self.orientation + beta) % (2 * pi)
    # end copied code

    else:
        # code referenced from https://gatech.instructure.com/courses/192324/pages/4-circular-motion-answer?module_item_id=1634086

        # Calculate turning radius
        turning_radius = new_distance / beta

        # calculate new x and y coordinates
        cx = self.x - (sin(self.orientation) * turning_radius)
        cy = self.y + (cos(self.orientation) * turning_radius)

        myrobot.x = cx + (sin(self.orientation + beta) * turning_radius)
        myrobot.y = cy - (cos(self.orientation + beta) * turning_radius)
        myrobot.orientation = (self.orientation + beta) % (2 * pi)
        # end copied code

    return myrobot  # make sure your move function returns an instance
    # of the robot class with the correct coordinates.


# QUESTION 5


def q5_sense(self, add_noise):
    # You can replace the INSIDE of this function with the sense function you modified in the module quiz
    # You can ignore add_noise for Q5
    Z = []

    # ENTER CODE HERE
    # HINT: You will probably need to use the function atan2()
    for i in range(len(landmarks)):
        y_l, x_l = landmarks[i][0], landmarks[i][1]

        delta_x = x_l - self.x
        delta_y = y_l - self.y
        bearing_angle = (atan2(delta_y, delta_x) - self.orientation) % (2 * pi)

        Z.append(bearing_angle)

    return Z  # Leave this line here. Return vector Z of 4 bearings.


# QUESTION 6


def q6_move(self, motion):
    # You can replace the INSIDE of this function with the move function you modified in the module quiz
    # Note that you will need to handle motion noise inside your function accordingly
    myrobot = robot()

    # Copy instance attributes to new object
    myrobot.length = self.length
    myrobot.orientation = self.orientation
    myrobot.bearing_noise = self.bearing_noise
    myrobot.distance_noise = self.distance_noise
    myrobot.steering_noise = self.steering_noise

    # Set noise for steering and distance
    new_steering = random.gauss(motion[0], self.steering_noise)
    new_distance = random.gauss(motion[1], self.distance_noise)

    # Calculate the turning angle
    beta = (tan(new_steering) * new_distance) / myrobot.length

    # code referenced from https://gatech.instructure.com/courses/192324/pages/4-circular-motion-answer?module_item_id=1634086
    # Check to see if beta is really small (I.e. basically completely straight forward motion)
    # Model straight forward motion
    if abs(beta) < 0.001:
        myrobot.x = self.x + (new_distance * cos(self.orientation))
        myrobot.y = self.y + (new_distance * sin(self.orientation))
        myrobot.orientation = (self.orientation + beta) % (2 * pi)
    # end copied code

    else:
        # code referenced from https://gatech.instructure.com/courses/192324/pages/4-circular-motion-answer?module_item_id=1634086

        # Calculate turning radius
        turning_radius = new_distance / beta

        # calculate new x and y coordinates
        cx = self.x - (sin(self.orientation) * turning_radius)
        cy = self.y + (cos(self.orientation) * turning_radius)

        myrobot.x = cx + (sin(self.orientation + beta) * turning_radius)
        myrobot.y = cy - (cos(self.orientation + beta) * turning_radius)
        myrobot.orientation = (self.orientation + beta) % (2 * pi)
        # end copied code

    return myrobot  # make sure your move function returns an instance


def q6_sense(self, add_noise=1):
    # You can replace the INSIDE of this function with what you changed in the module quiz
    # Note the add_noise parameter is passed to sense()
    Z = []

    # ENTER CODE HERE
    # HINT: You will probably need to use the function atan2()
    for i in range(len(landmarks)):
        y_l, x_l = landmarks[i][0], landmarks[i][1]

        delta_x = x_l - self.x
        delta_y = y_l - self.y
        bearing_angle = (atan2(delta_y, delta_x) - self.orientation) % (2 * pi)

        # Code referenced from: https://gatech.instructure.com/courses/213570/pages/5-sensing-answer?module_item_id=1891178
        if add_noise:
            bearing_angle += random.gauss(0.0, self.bearing_noise)
            bearing_angle = bearing_angle % (2 * pi)
        # end copied code

        Z.append(bearing_angle)

    return Z


######################################################################
# Grading methods
#
# Do not modify code below this point.
#
# The auto-grader does not use any of the below code
#
######################################################################
landmarks = [
    [0.0, 100.0],
    [0.0, 0.0],
    [100.0, 0.0],
    [100.0, 100.0],
]  # landmarks are in (y, x) format
world_size = 100.0
tolerance_xy = 15.0  # Tolerance for localization in the x and y directions.
tolerance_orientation = 0.25  # Tolerance for orientation.


class robot(object):
    move_func_name = None  # used to control which move function is used by robot instance
    sense_func_name = None  # used to control which sense function is used by robot instance

    def __init__(self, length=10.0):
        self.x = random.random() * world_size  # initial x position
        self.y = random.random() * world_size  # initial y position
        self.orientation = random.random() * 2.0 * pi  # initial orientation
        self.length = length  # length of robot
        self.bearing_noise = 0.0  # initialize bearing noise to zero
        self.steering_noise = 0.0  # initialize steering noise to zero
        self.distance_noise = 0.0  # initialize distance noise to zero
        self.move_func = globals().get(robot.move_func_name)
        self.sense_func = globals().get(robot.sense_func_name)

    def __repr__(self):
        return "[x=%.6s y=%.6s orient=%.6s]" % (str(self.x), str(self.y), str(self.orientation))

    def set(self, new_x, new_y, new_orientation):

        if new_orientation < 0 or new_orientation >= 2 * pi:
            raise ValueError("Orientation must be in [0..2pi]")
        self.x = float(new_x)
        self.y = float(new_y)
        self.orientation = float(new_orientation)

    def set_noise(self, new_b_noise, new_s_noise, new_d_noise):
        self.bearing_noise = float(new_b_noise)
        self.steering_noise = float(new_s_noise)
        self.distance_noise = float(new_d_noise)

    def measurement_prob(self, measurements):
        predicted_measurements = self.sense(0)

        if not isinstance(predicted_measurements, list) and not isinstance(
            predicted_measurements, tuple
        ):
            raise RuntimeError(
                "sense() expected to return a list, instead got %s" % type(predicted_measurements)
            )

        if len(predicted_measurements) != len(measurements):
            raise RuntimeError(
                "%d measurements but %d predicted measurements from sense"
                % (len(measurements), len(predicted_measurements))
            )

        error = 1.0
        for i in range(len(measurements)):
            error_bearing = abs(measurements[i] - predicted_measurements[i])
            error_bearing = (error_bearing + pi) % (2.0 * pi) - pi

            error *= old_div(
                exp(old_div(-(error_bearing ** 2), (self.bearing_noise ** 2)) / 2.0),
                sqrt(2.0 * pi * (self.bearing_noise ** 2)),
            )

        return error

    def move(self, motion):
        if self.move_func is not None:
            return self.move_func(self, motion)
        else:
            return self

    def sense(self, add_noise=1):
        if self.sense_func is not None:
            return self.sense_func(self, add_noise)
        else:
            return []


def get_position(p):
    x = 0.0
    y = 0.0
    orientation = 0.0
    for i in range(len(p)):
        x += p[i].x
        y += p[i].y
        orientation += (
            ((p[i].orientation - p[0].orientation + pi) % (2.0 * pi)) + p[0].orientation - pi
        )
    return [old_div(x, len(p)), old_div(y, len(p)), old_div(orientation, len(p))]


def float_to_str(x):
    return "%.04f" % x


def list_of_float_to_str(lst):
    return str(list(map(float_to_str, lst)))


FILL_IN_TEST_CASES = (
    {
        "variable_name": "q1_n_1",
        "str_func": float_to_str,
        "answer_hash": "42f2d990b0d1b069fcc6952dcf8e03f5",
        "points_avail": 1.0 / 3.0,
    },
    {
        "variable_name": "q1_n_4",
        "str_func": float_to_str,
        "answer_hash": "cd6b6a8e6aca6a3bf5b914b2eb1d471e",
        "points_avail": 1.0 / 3.0,
    },
    {
        "variable_name": "q1_n_10",
        "str_func": float_to_str,
        "answer_hash": "162d0da51e5b91c22b8ef816a33b93ae",
        "points_avail": 1.0 / 3.0,
    },
    {
        "variable_name": "q2_1_step_A",
        "str_func": float_to_str,
        "answer_hash": "4c519e55122fb9103f3429d4d35246c2",
        "points_avail": 1.0 / 8.0,
    },
    {
        "variable_name": "q2_1_step_B",
        "str_func": float_to_str,
        "answer_hash": "865f680967fee7bab877431d55a667e9",
        "points_avail": 1.0 / 8.0,
    },
    {
        "variable_name": "q2_1_step_C",
        "str_func": float_to_str,
        "answer_hash": "48482b0046ab77768ab1471544d39c03",
        "points_avail": 1.0 / 8.0,
    },
    {
        "variable_name": "q2_1_step_D",
        "str_func": float_to_str,
        "answer_hash": "b67dd96cc694c9beac33d9fbd459174c",
        "points_avail": 1.0 / 8.0,
    },
    {
        "variable_name": "q2_infinite_step_A",
        "str_func": float_to_str,
        "answer_hash": "eff0c2c81ea4c663110ccca7da9783c9",
        "points_avail": 1.0 / 8.0,
    },
    {
        "variable_name": "q2_infinite_step_B",
        "str_func": float_to_str,
        "answer_hash": "3e74f80dcde13f3e2d4016ccfdb3e6fd",
        "points_avail": 1.0 / 8.0,
    },
    {
        "variable_name": "q2_infinite_step_C",
        "str_func": float_to_str,
        "answer_hash": "32e9394cabcb64eb6fe926fd18f7eea1",
        "points_avail": 1.0 / 8.0,
    },
    {
        "variable_name": "q2_infinite_step_D",
        "str_func": float_to_str,
        "answer_hash": "b6a07a19e607d0686dfc627c139c373f",
        "points_avail": 1.0 / 8.0,
    },
    {
        "variable_name": "q3_works_fine",
        "str_func": float_to_str,
        "answer_hash": "ab5378bc6072dac87d8eae185c1d5a50",
        "points_avail": 1.0 / 5.0,
    },
    {
        "variable_name": "q3_ignores_robot_measurements",
        "str_func": float_to_str,
        "answer_hash": "85f15f9ddfad3555ce7f803375591fcb",
        "points_avail": 1.0 / 5.0,
    },
    {
        "variable_name": "q3_ignores_robot_motion",
        "str_func": float_to_str,
        "answer_hash": "a16592a0343fcca9b90b5220ac53491b",
        "points_avail": 1.0 / 5.0,
    },
    {
        "variable_name": "q3_it_likely_fails",
        "str_func": float_to_str,
        "answer_hash": "945f27265e22c511bb56f1631610442a",
        "points_avail": 1.0 / 5.0,
    },
    {
        "variable_name": "q3_none_of_above",
        "str_func": float_to_str,
        "answer_hash": "c885bdcdfbd4a9f353ee68f7be7dbf9e",
        "points_avail": 1.0 / 5.0,
    },
)

# PROGRAMMING


def grader_q4(
    length=20,
    x=0.0,
    y=0.0,
    orientation=0.0,
    bearing_noise=0.0,
    steering_noise=0.0,
    distance_noise=0.0,
    motions=(),
):
    robot.move_func_name = "q4_move"

    outputs = []

    grader_robot = robot(length)
    grader_robot.set(x, y, orientation)
    grader_robot.set_noise(bearing_noise, steering_noise, distance_noise)

    for motion in motions:
        grader_robot = grader_robot.move(motion)
        outputs.append((grader_robot.x, grader_robot.y, grader_robot.orientation))

    return outputs


def grader_q5(
    length=20,
    x=0.0,
    y=0.0,
    orientation=0.0,
    bearing_noise=0.0,
    steering_noise=0.0,
    distance_noise=0.0,
):

    robot.sense_func_name = "q5_sense"

    grader_robot = robot(length)
    grader_robot.set(x, y, orientation)
    grader_robot.set_noise(bearing_noise, steering_noise, distance_noise)
    return grader_robot.sense()


def grader_q6(
    length=20,
    bearing_noise=0.0,
    steering_noise=0.0,
    distance_noise=0.0,
    motions=(),
    measurements=(),
    N=100,
):

    robot.move_func_name = "q6_move"
    robot.sense_func_name = "q6_sense"
    result = ""
    points_earned = 0

    p = []

    for i in range(N):
        r = robot(length=length)
        r.set_noise(bearing_noise, steering_noise, distance_noise)
        p.append(r)

    for t in range(len(motions)):
        p2 = []
        for i in range(N):
            p2.append(p[i].move(motions[t]))
        p = p2

        w = []
        for i in range(N):
            w.append(p[i].measurement_prob(measurements[t]))

        p3 = []
        index = int(random.random() * N) % N
        beta = 0.0
        mw = max(w)
        for i in range(N):
            beta += random.random() * 2.0 * mw
            while beta > w[index]:
                beta -= w[index]
                index = (index + 1) % N
            p3.append(p[index])
        p = p3

    return get_position(p)


def q4_output_match(values, expected):
    temp = True
    if len(values) != len(expected):
        return False
    else:
        for t in range(len(values)):
            if not (
                abs(values[t][0] - expected[t][0]) < 0.01
                and abs(values[t][1] - expected[t][1]) < 0.01
                and abs(values[t][2] - expected[t][2]) < 0.01
            ):
                temp = False
                break
    return temp


def q5_output_match(values, expected):
    temp = True
    if len(values) != len(expected):
        return False
    else:
        for t in range(len(values)):
            if not (abs(values[t] - expected[t]) < 0.01):
                temp = False
                break
    return temp


def q6_check_output(pos0, pos1):

    error_x = abs(pos0[0] - pos1[0])
    error_y = abs(pos0[1] - pos1[1])
    error_orientation = abs(pos0[2] - pos1[2])
    error_orientation = (error_orientation + pi) % (2.0 * pi) - pi
    correct = (
        error_x < tolerance_xy
        and error_y < tolerance_xy
        and error_orientation < tolerance_orientation
    )
    return correct


CODE_TEST_CASES = (
    {
        "function_name": "grader_q4",
        "function_input": dict(
            length=20.0,
            x=0.0,
            y=0.0,
            orientation=0.0,
            bearing_noise=0.0,
            steering_noise=0.0,
            distance_noise=0.0,
            motions=[(0.0, 10.0), (pi / 6.0, 10), (0.0, 20.0)],
        ),
        "expected_output": [(10.0, 0.0, 0.0), (19.861, 1.4333, 0.2886), (39.034, 7.127, 0.2886)],
        "outputs_match_func": lambda actual, expected: q4_output_match(actual, expected),
        "output_to_str_func": list_of_float_to_str,
    },
    {
        "function_name": "grader_q5",
        "function_input": dict(
            length=20.0,
            x=30.0,
            y=20.0,
            orientation=0.0,
            bearing_noise=0.0,
            steering_noise=0.0,
            distance_noise=0.0,
        ),
        "expected_output": [
            6.004885648174475,
            3.7295952571373605,
            1.9295669970654687,
            0.8519663271732721,
        ],
        "outputs_match_func": lambda actual, expected: q5_output_match(actual, expected),
        "output_to_str_func": list_of_float_to_str,
    },
    {
        "function_name": "grader_q6",
        "function_input": dict(
            length=20.0,
            bearing_noise=0.1,
            steering_noise=0.1,
            distance_noise=5.0,
            motions=[(old_div(2.0 * pi, 10), 20.0) for row in range(8)],
            measurements=[
                [4.746936, 3.859782, 3.045217, 2.045506],
                [3.510067, 2.916300, 2.146394, 1.598332],
                [2.972469, 2.407489, 1.588474, 1.611094],
                [1.906178, 1.193329, 0.619356, 0.807930],
                [1.352825, 0.662233, 0.144927, 0.799090],
                [0.856150, 0.214590, 5.651497, 1.062401],
                [0.194460, 5.660382, 4.761072, 2.471682],
                [5.717342, 4.736780, 3.909599, 2.342536],
            ],
        ),
        "expected_output": [93.476, 75.186, 5.2664],
        "outputs_match_func": q6_check_output,
        "output_to_str_func": list_of_float_to_str,
        "tries": 20,
        "matches_required": 12,
    },
)

if __name__ == "__main__":
    import checkutil

    checkutil.check(FILL_IN_TEST_CASES, CODE_TEST_CASES, locals())
