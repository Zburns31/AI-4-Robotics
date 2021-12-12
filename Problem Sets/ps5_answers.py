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
# solution_check
#   For fill-in questions, change the value of each answer variable.
#
#   For programming questions, change the implementation of the
#   function provided.
#
#   Run the file from the command line to check:
#
#       python ps5_answers.py
#
######################################################################

from __future__ import division
from __future__ import print_function
from builtins import zip
from builtins import str
from builtins import range
from builtins import object
from past.utils import old_div
from copy import deepcopy

# If you see different scores locally and on Gradescope this may be an indication
# that you are uploading a different file than the one you are executing locally.
# If this local ID doesn't match the ID on Gradescope then you uploaded a different file.
OUTPUT_UNIQUE_FILE_ID = False
if OUTPUT_UNIQUE_FILE_ID:
    import hashlib, pathlib

    file_hash = hashlib.md5(pathlib.Path(__file__).read_bytes()).hexdigest()
    print(f"Unique file ID: {file_hash}")

# STUDENT ID
#
# Please specify your GT login ID in the whoami variable (ex: jsmith321).
#

whoami = "zburns6"

# Question 1: MISSING PARAMETERS
#
# How does the variance of the new Gaussian compare to the individual Guassians?
#
possible_answers = ("Tp = 0", "Td = 0", "Ti = 0", "No Problem")
# Question 1, part A
#
# What is step one?
#
one = "Td = 0"

# Question 1, part B
#
# What is step two?
#
two = "No Problem"

# Question 1, part C
#
# What is step three?
#
three = "Ti = 0"

# Question 1, part D
#
# What is step four?
#
four = "Tp = 0"


# Question 2: CYCLIC SMOOTHING
#
# -------------
# User Instructions
#
# Here you will be implementing a cyclic smoothing
# algorithm. This algorithm should not fix the end
# points (as you did in the unit quizzes). You
# should use the gradient descent equations that
# you used previously.
#
# Your function should return the newpath that it
# calculates.
#
# Feel free to use the provided solution_check function
# to test your code. You can find it at the bottom.
#
# --------------
# Testing Instructions
#
# To test your code, call the solution_check function with
# two arguments. The first argument should be the result of your
# smooth function. The second should be the corresponding answer.
# For example, calling
#
# solution_check(smooth(testpath1), answer1)
#
# should return True if your answer is correct and False if
# it is not.

from math import *

# Do not modify path inside your function.
path = [
    [0, 0],
    [1, 0],
    [2, 0],
    [3, 0],
    [4, 0],
    [5, 0],
    [6, 0],
    [6, 1],
    [6, 2],
    [6, 3],
    [5, 3],
    [4, 3],
    [3, 3],
    [2, 3],
    [1, 3],
    [0, 3],
    [0, 2],
    [0, 1],
]

############# ONLY ENTER CODE BELOW THIS LINE ##########

# ------------------------------------------------
# smooth coordinates
# NOTE: Check the errata below the video in Canvas about only updating newpath once per iteration
#


def smooth(path, weight_data=0.1, weight_smooth=0.1, tolerance=0.00001):

    #
    # Enter code here
    #
    newpath = deepcopy(path)
    change = tolerance
    while change >= tolerance:
        change = 0.0
        for i in range(len(newpath)):
            for j in range(len(newpath[0])):
                # code referenced from: https://gatech.instructure.com/courses/213570/pages/2-cyclic-smoothing-answer?module_item_id=1891416
                aux = newpath[i][j]
                newpath[i][j] += weight_data * (path[i][j] - newpath[i][j]) + weight_smooth * (
                    newpath[(i - 1) % len(path)][j]
                    + newpath[(i + 1) % len(path)][j]
                    - 2.0 * newpath[i][j]
                )
                change += abs(aux - newpath[i][j])
                # end copied code
    return newpath


# thank you - EnTerr - for posting this on our discussion forum

# newpath = smooth(path)
# for i in range(len(path)):
#    print '['+ ', '.join('%.3f'%x for x in path[i]) +'] -> ['+ ', '.join('%.3f'%x for x in newpath[i]) +']'


##### TESTING ######

# --------------------------------------------------
# check if two numbers are 'close enough,'used in
# solution_check function.
#
def close_enough(user_answer, true_answer, epsilon=0.0001):
    if abs(user_answer - true_answer) > epsilon:
        return False
    return True


# --------------------------------------------------
# check your solution against our reference solution for
# a variety of test cases (given below)
#
def solution_check(newpath, answer, printflag=False):

    if type(newpath) != type(answer):
        print("Error. You do not return a list.")
        return False
    if len(newpath) != len(answer):
        print("Error. Your newpath is not the correct length.")
        return False
    if len(newpath[0]) != len(answer[0]):
        print("Error. Your entries do not contain an (x, y) coordinate pair.")
        return False
    for i in range(len(newpath)):
        for j in range(len(newpath[0])):
            if not close_enough(newpath[i][j], answer[i][j]):
                print("Error, at least one of your entries is not correct.")
                return False
    if printflag:
        print("Test case correct!")
    return True


# --------------
# Testing Instructions
#
# To test your code, call the solution_check function with
# two arguments. The first argument should be the result of your
# smooth function. The second should be the corresponding answer.
# For example, calling
#
# solution_check(smooth(testpath1), answer1)
#
# should return True if your answer is correct and False if
# it is not.

testpath1 = [
    [0, 0],
    [1, 0],
    [2, 0],
    [3, 0],
    [4, 0],
    [5, 0],
    [6, 0],
    [6, 1],
    [6, 2],
    [6, 3],
    [5, 3],
    [4, 3],
    [3, 3],
    [2, 3],
    [1, 3],
    [0, 3],
    [0, 2],
    [0, 1],
]

answer1 = [
    [0.4705860385182691, 0.4235279620576893],
    [1.1764695730296597, 0.16470408411716733],
    [2.058823799247812, 0.07058633859438503],
    [3.000001503542886, 0.04705708651959327],
    [3.9411790099468273, 0.07058689299792453],
    [4.8235326678889345, 0.16470511854183797],
    [5.529415336860586, 0.4235293374365447],
    [5.76470933698621, 1.1058829941330384],
    [5.764708805535902, 1.8941189433780983],
    [5.5294138118186265, 2.5764724018811056],
    [4.823530348360371, 2.835296251305122],
    [3.941176199414957, 2.929413985845729],
    [2.9999985709076413, 2.952943245204772],
    [2.0588211310939526, 2.9294134622132018],
    [1.1764675231284938, 2.8352952720424938],
    [0.4705848811030855, 2.5764710948028178],
    [0.23529088056307781, 1.8941174802285707],
    [0.23529138316655338, 1.1058815684272394],
]

testpath2 = [
    [1, 0],  # Move in the shape of a plus sign
    [2, 0],
    [2, 1],
    [3, 1],
    [3, 2],
    [2, 2],
    [2, 3],
    [1, 3],
    [1, 2],
    [0, 2],
    [0, 1],
    [1, 1],
]

answer2 = [
    [1.2222234770374059, 0.4444422843711052],
    [1.7777807251383388, 0.4444432993123497],
    [2.111114925633848, 0.8888894279539462],
    [2.5555592020540376, 1.2222246475393077],
    [2.5555580686154244, 1.7777817817879298],
    [2.111111849558437, 2.1111159707965514],
    [1.7777765871460525, 2.55556033483712],
    [1.2222194640861452, 2.5555593592828543],
    [0.8888853322565222, 2.111113321684573],
    [0.44444105139827167, 1.777778212019149],
    [0.44444210978390364, 1.2222211690821811],
    [0.8888882042812255, 0.8888870211766268],
]


def cyclic():
    return solution_check(smooth(testpath1), answer1)


# solution_check(smooth(testpath1), answer1)
# solution_check(smooth(testpath2), answer2)


# Question 3: CONSTRAINED SMOOTHING
#
# -------------
# User Instructions
#
# Now you will be incorporating fixed points into
# your smoother.
#
# You will need to use the equations from gradient
# descent AND the new equations presented in the
# previous lecture to implement smoothing with
# fixed points.
#
# Your function should return the newpath that it
# calculates.
#
# Feel free to use the provided solution_check function
# to test your code. You can find it at the bottom.
#

######################## ENTER CODE BELOW HERE #########################


def smooth2(path, fix, weight_data=0.0, weight_smooth=0.1, tolerance=0.00001):
    #
    # Enter code here.
    # The weight for each of the two new equations should be 0.5 * weight_smooth
    #
    newpath = deepcopy(path)
    change = tolerance
    while change >= tolerance:
        change = 0.0
        for i in range(len(newpath)):
            # code referenced from: https://gatech.instructure.com/courses/213570/pages/3-constrained-smoothing?module_item_id=1891418
            if not fix[i]:
                for j in range(len(newpath[0])):
                    aux = newpath[i][j]
                    newpath[i][j] += (
                        weight_smooth
                        * (
                            newpath[(i - 1) % len(path)][j]
                            + newpath[(i + 1) % len(path)][j]
                            - 2.0 * newpath[i][j]
                        )
                        + (weight_smooth / 2.0)
                        * (
                            2.0 * newpath[(i - 1) % len(path)][j]
                            - newpath[(i - 2) % len(path)][j]
                            - newpath[i][j]
                        )
                        + (weight_smooth / 2.0)
                        * (
                            2.0 * newpath[(i + 1) % len(path)][j]
                            - newpath[(i + 2) % len(path)][j]
                            - newpath[i][j]
                        )
                    )
                    change += abs(aux - newpath[i][j])
                    # end copied code
    return newpath


# --------------
# Testing Instructions
#
# To test your code, call the solution_check function with the argument smooth:
# solution_check(smooth)
#


def solution_check2(smooth2, eps=0.0001, printflag=False):
    def test_case_str(path, fix):
        assert len(path) == len(fix)
        if len(path) == 0:
            return "[]"
        if len(path) == 1:
            s = "[" + str(path[0]) + "]"
            if fix[0]:
                s += " #fix"
            return s

        s = "[" + str(path[0]) + ","
        if fix[0]:
            s += " #fix"
        for pt, f in zip(path[1:-1], fix[1:-1]):
            s += "\n " + str(pt) + ","
            if f:
                s += " #fix"
        s += "\n " + str(path[-1]) + "]"
        if fix[-1]:
            s += " #fix"
        return s

    testpaths = [
        [
            [0, 0],
            [1, 0],
            [2, 0],
            [3, 0],
            [4, 0],
            [5, 0],
            [6, 0],
            [6, 1],
            [6, 2],
            [6, 3],
            [5, 3],
            [4, 3],
            [3, 3],
            [2, 3],
            [1, 3],
            [0, 3],
            [0, 2],
            [0, 1],
        ],
        [[0, 0], [2, 0], [4, 0], [4, 2], [4, 4], [2, 4], [0, 4], [0, 2]],
    ]
    testfixpts = [[1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0], [1, 0, 1, 0, 1, 0, 1, 0]]
    pseudo_answers = [
        [
            [0, 0],
            [0.7938620981547201, -0.8311168821106101],
            [1.8579052986461084, -1.3834788165869276],
            [3.053905318597796, -1.5745863173084],
            [4.23141390533387, -1.3784271816058231],
            [5.250184859723701, -0.8264215958231558],
            [6, 0],
            [6.415150091996651, 0.9836951698796843],
            [6.41942442687092, 2.019512290770163],
            [6, 3],
            [5.206131365604606, 3.831104483245191],
            [4.142082497497067, 4.383455704596517],
            [2.9460804122779813, 4.5745592975708105],
            [1.768574219397359, 4.378404668718541],
            [0.7498089205417316, 3.826409771585794],
            [0, 3],
            [-0.4151464728194156, 2.016311854977891],
            [-0.4194207879552198, 0.9804948340550833],
        ],
        [
            [0, 0],
            [2.0116767115496095, -0.7015439080661671],
            [4, 0],
            [4.701543905420104, 2.0116768147460418],
            [4, 4],
            [1.9883231877640861, 4.701543807525115],
            [0, 4],
            [-0.7015438099112995, 1.9883232808252207],
        ],
    ]
    true_answers = [
        [
            [0, 0],
            [0.7826068175979299, -0.6922616156406778],
            [1.826083356960912, -1.107599209206985],
            [2.999995745732953, -1.2460426422963626],
            [4.173909508264126, -1.1076018591282746],
            [5.217389489606966, -0.6922642758483151],
            [6, 0],
            [6.391305105067843, 0.969228211275216],
            [6.391305001845138, 2.0307762911524616],
            [6, 3],
            [5.217390488523538, 3.6922567975830876],
            [4.17391158149052, 4.107590195596796],
            [2.9999982969959467, 4.246032043344827],
            [1.8260854997325473, 4.107592961155283],
            [0.7826078838205919, 3.692259569132191],
            [0, 3],
            [-0.3913036785959153, 2.030774470796648],
            [-0.3913035729270973, 0.9692264531461132],
        ],
        [
            [0, 0],
            [1.9999953708444873, -0.6666702980585777],
            [4, 0],
            [4.666670298058577, 2.000005101453379],
            [4, 4],
            [1.9999948985466212, 4.6666612524128],
            [0, 4],
            [-0.6666612524127998, 2.000003692691148],
        ],
    ]
    newpaths = [smooth2(*p) for p in zip(testpaths, testfixpts)]

    correct = True

    for path, fix, p_answer, t_answer, newpath in zip(
        testpaths, testfixpts, pseudo_answers, true_answers, newpaths
    ):
        if type(newpath) != list:
            if printflag:
                print("Error: smooth did not return a list for the path:")
                print(test_case_str(path, fix) + "\n")
            correct = False
            continue
        if len(newpath) != len(path):
            if printflag:
                print("Error: smooth did not return a list of the correct length for the path:")
                print(test_case_str(path, fix) + "\n")
            correct = False
            continue

        good_pairs = True
        for newpt, pt in zip(newpath, path):
            if len(newpt) != len(pt):
                good_pairs = False
                break
        if not good_pairs:
            if printflag:
                print("Error: smooth did not return a list of coordinate pairs for the path:")
                print(test_case_str(path, fix) + "\n")
            correct = False
            continue

        # check whether to check against true or pseudo answers
        answer = None
        if abs(newpath[1][0] - t_answer[1][0]) <= eps:
            answer = t_answer
        elif abs(newpath[1][0] - p_answer[1][0]) <= eps:
            answer = p_answer
        else:
            if printflag:
                print("smooth returned an incorrect answer for the path:")
                print(test_case_str(path, fix) + "\n")
            correct = False
            continue

        entries_match = True
        for p, q in zip(newpath, answer):
            for pi, qi in zip(p, q):
                if abs(pi - qi) > eps:
                    entries_match = False
                    break
            if not entries_match:
                break
        if not entries_match:
            if printflag:
                print("smooth returned an incorrect answer for the path:")
                print(test_case_str(path, fix) + "\n")
            correct = False
            continue

        if answer == t_answer:
            if printflag:
                print("smooth returned the correct answer for the path:")
                print(test_case_str(path, fix) + "\n")
        elif answer == p_answer:
            if printflag:
                print("smooth returned a correct* answer for the path:")
                print(test_case_str(path, fix))
                print(
                    """*However, your answer uses the "nonsimultaneous" update method, which
    is not technically correct. You should modify your code so that newpath[i][j] is only
    updated once per iteration, or else the intermediate updates made to newpath[i][j]
    will affect the final answer.\n"""
                )
    return correct


def constrained():
    return solution_check2(smooth2)


# solution_check(smooth)


# Question 4: RACETRACK CONTROL
#
# --------------
# User Instructions
#
# Define a function cte in the robot class that will
# compute the crosstrack error for a robot on a
# racetrack with a shape as described in the video.
#
# You will need to base your error calculation on
# the robot's location on the track. Remember that
# the robot will be traveling to the right on the
# upper straight segment and to the left on the lower
# straight segment.
#
# --------------
# Grading Notes
#
# We will be testing your cte function directly by
# calling it with different robot locations and making
# sure that it returns the correct crosstrack error.

from math import *
import random


# ------------------------------------------------
#
# this is the robot class
#


class robot(object):

    # --------
    # init:
    #    creates robot and initializes location/orientation to 0, 0, 0
    #

    def __init__(self, length=20.0):
        self.x = 0.0
        self.y = 0.0
        self.orientation = 0.0
        self.length = length
        self.steering_noise = 0.0
        self.distance_noise = 0.0
        self.steering_drift = 0.0

    # --------
    # set:
    # 	sets a robot coordinate
    #

    def set(self, new_x, new_y, new_orientation):

        self.x = float(new_x)
        self.y = float(new_y)
        self.orientation = float(new_orientation) % (2.0 * pi)

    # --------
    # set_noise:
    # 	sets the noise parameters
    #

    def set_noise(self, new_s_noise, new_d_noise):
        # makes it possible to change the noise parameters
        # this is often useful in particle filters
        self.steering_noise = float(new_s_noise)
        self.distance_noise = float(new_d_noise)

    # --------
    # set_steering_drift:
    # 	sets the systematical steering drift parameter
    #

    def set_steering_drift(self, drift):
        self.steering_drift = drift

    # --------
    # move:
    #    steering = front wheel steering angle, limited by max_steering_angle
    #    distance = total distance driven, most be non-negative

    def move(self, steering, distance, tolerance=0.001, max_steering_angle=pi / 4.0):

        if steering > max_steering_angle:
            steering = max_steering_angle
        if steering < -max_steering_angle:
            steering = -max_steering_angle
        if distance < 0.0:
            distance = 0.0

        # make a new copy
        res = robot()
        res.length = self.length
        res.steering_noise = self.steering_noise
        res.distance_noise = self.distance_noise
        res.steering_drift = self.steering_drift

        # apply noise
        steering2 = random.gauss(steering, self.steering_noise)
        distance2 = random.gauss(distance, self.distance_noise)

        # apply steering drift
        steering2 += self.steering_drift

        # Execute motion
        turn = old_div(tan(steering2) * distance2, res.length)

        if abs(turn) < tolerance:

            # approximate by straight line motion

            res.x = self.x + (distance2 * cos(self.orientation))
            res.y = self.y + (distance2 * sin(self.orientation))
            res.orientation = (self.orientation + turn) % (2.0 * pi)

        else:

            # approximate bicycle model for motion

            radius = old_div(distance2, turn)
            cx = self.x - (sin(self.orientation) * radius)
            cy = self.y + (cos(self.orientation) * radius)
            res.orientation = (self.orientation + turn) % (2.0 * pi)
            res.x = cx + (sin(res.orientation) * radius)
            res.y = cy - (cos(res.orientation) * radius)

        return res

    def __repr__(self):
        return "[x=%.5f y=%.5f orient=%.5f]" % (self.x, self.y, self.orientation)

    ############## ONLY ADD / MODIFY CODE BELOW THIS LINE ####################

    def cte(self, radius):
        #
        cte = 5
        # Add code here
        #
        #
        x = self.x
        y = self.y

        # code referenced from here: https://classroom.udacity.com/courses/cs373/lessons/48721468/concepts/487015300923
        if x < radius:
            dist = sqrt((x - radius) ** 2 + (y - radius) ** 2)
            cte = dist - radius

        elif x > 3.0 * radius:
            dist = sqrt((x - 3.0 * radius) ** 2 + (y - radius) ** 2)
            cte = dist - radius

        elif y > radius:
            cte = y - 2.0 * radius

        else:
            cte = -y
        # end copied code
        return cte


############## ONLY ADD / MODIFY CODE ABOVE THIS LINE ####################


# ------------------------------------------------------------------------
#
# run - does a single control run.


def run(params, radius, printflag=False):
    myrobot = robot()
    myrobot.set(0.0, radius, pi / 2.0)
    speed = 1.0  # motion distance is equal to speed (we assume time = 1)
    err = 0.0
    int_crosstrack_error = 0.0
    N = 200

    crosstrack_error = myrobot.cte(radius)  # You need to define the cte function!

    for i in range(N * 2):
        diff_crosstrack_error = -crosstrack_error
        crosstrack_error = myrobot.cte(radius)
        diff_crosstrack_error += crosstrack_error
        int_crosstrack_error += crosstrack_error
        steer = (
            -params[0] * crosstrack_error
            - params[1] * diff_crosstrack_error
            - params[2] * int_crosstrack_error
        )
        myrobot = myrobot.move(steer, speed)
        if i >= N:
            err += crosstrack_error ** 2
        if printflag:
            print(myrobot)
    return err / float(N)


def racetrack(printflag=False):
    radius = 25.0
    params = [10.0, 15.0, 0]
    err = run(params, radius, False)
    if printflag:
        print("\nFinal parameters: ", params, "\n ->", err)
    if err < 0.1:
        return True
    else:
        return False


######################################################################
# How to check:
#
#   python ps5_answers.py
#
######################################################################

float_to_str = lambda x: "%.04f" % x
bool_to_str = lambda x: str(x)
do_nothing = lambda x: x

FILL_IN_TEST_CASES = (
    {
        "variable_name": "one",
        "str_func": do_nothing,
        "answer_hash": "8ad511191de81011057f790676e2bf57",
        "points_avail": 1,
    },
    {
        "variable_name": "two",
        "str_func": do_nothing,
        "answer_hash": "ec6350ea46cb209093e40529134f4728",
        "points_avail": 1,
    },
    {
        "variable_name": "three",
        "str_func": do_nothing,
        "answer_hash": "136c6d5608c72354ef2a99ff17be8bc6",
        "points_avail": 1,
    },
    {
        "variable_name": "four",
        "str_func": do_nothing,
        "answer_hash": "3a1c83f56f7712e8677ea7eea3ec2c2f",
        "points_avail": 1,
    },
)


def equivalent(arr0, arr1):
    return arr0 == arr1


CODE_TEST_CASES = (
    {
        "function_name": "cyclic",
        "function_input": dict(),
        "expected_output": True,
        "outputs_match_func": equivalent,
        "output_to_str_func": bool_to_str,
        "points_avail": 2,
    },
    {
        "function_name": "constrained",
        "function_input": dict(),
        "expected_output": True,
        "outputs_match_func": equivalent,
        "output_to_str_func": bool_to_str,
        "points_avail": 2,
    },
    {
        "function_name": "run",
        "function_input": dict(radius=25.0, params=[10.0, 15.0, 0.0], printflag=True),
        "expected_output": 0.0059,
        "outputs_match_func": lambda actual, expected: abs(actual - expected) < 0.0001,
        "output_to_str_func": float_to_str,
        "points_avail": 2,
    },
)

if __name__ == "__main__":
    import checkutil

    checkutil.check(FILL_IN_TEST_CASES, CODE_TEST_CASES, locals())
