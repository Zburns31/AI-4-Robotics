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
#       python ps2_answers.py
#
######################################################################

# If you see different scores locally and on Gradescope this may be an indication
# that you are uploading a different file than the one you are executing locally.
# If this local ID doesn't match the ID on Gradescope then you uploaded a different file.
OUTPUT_UNIQUE_FILE_ID = False
if OUTPUT_UNIQUE_FILE_ID:
    import hashlib, pathlib

    file_hash = hashlib.md5(pathlib.Path(__file__).read_bytes()).hexdigest()
    print(f"Unique file ID: {file_hash}")

# STUDENT ID

# Please specify your GT login ID in the whoami variable (ex: jsmith321).

whoami = "zburns6"

n = float("nan")

# Question 1: MEASUREMENT UPDATE
#
# How does the variance of the new Gaussian compare to the individual Guassians?
#
possible_answers = ("smaller", "larger", "the same")
update = "smaller"


# Question 2: NEW VARIANCE
#
# What is the value for Nu squared as a multiple of Sigma squared?
# Replace n with your answer
#
variance = 0.5


# Question 3: HEAVYTAIL GAUSSIAN
#
# Is it possible to represent this function as a Gaussian?
#
possible_answers = ("YES", "NO")
heavytail = "NO"


# QUESTION 4: HOW MANY DIMENSIONS
#
# How many dimensions of the state vector for 2-dimensional space?
# Replace n with your answer
#
dimensions = 4

# QUESTION 5: STATE TRANSITION MATRIX
#
# What is the new F matrix for a Kalman filter in 2 dimensions?
# Replace the n's with your answers
#
F = [[1, 0, 0.1, 0], [0, 1, 0, 0.1], [0, 0, 1, 0], [0, 0, 0, 1]]


# QUESTION 6: PROGRAMMING EXERCISE

# Fill in the matrices P, F, H, R and I at the bottom
#
# This question requires NO CODING, just fill in the
# matrices by replacing n with your values.
#
# Please do not delete or modify
# any provided code. Good luck!
#
Matrices_P = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1000, 0], [0, 0, 0, 1000]]

Matrices_F = [[1, 0, 0.1, 0], [0, 1, 0, 0.1], [0, 0, 1, 0], [0, 0, 0, 1]]

Matrices_H = [[1, 0, 0, 0], [0, 1, 0, 0]]

Matrices_R = [[0.1, 0], [0, 0.1]]

Matrices_I = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]


######################################################################
# Grading methods
#
# Do not modify code below this point.
#
######################################################################

import hashlib
import checkutil

float_to_str = lambda x: "%.04f" % x
do_nothing = lambda x: x

FILL_IN_TEST_CASES = (
    {
        "variable_name": "update",
        "str_func": do_nothing,
        "answer_hash": "43dd639229e914a5327206408c1287c0",
        "points_avail": 1,
    },
    {
        "variable_name": "variance",
        "str_func": float_to_str,
        "answer_hash": "2ea3bd7cc5760c8622dfc868bd505c4c",
        "points_avail": 1,
    },
    {
        "variable_name": "heavytail",
        "str_func": do_nothing,
        "answer_hash": "ef544ea31f6ea82b72384a7d9ef3dccf",
        "points_avail": 1,
    },
    {
        "variable_name": "dimensions",
        "str_func": float_to_str,
        "answer_hash": "efb95511d768395bb81769b61a33e0b8",
        "points_avail": 1,
    },
    {
        "variable_name": "F",
        "variable_idxs": (0, 0),
        "str_func": float_to_str,
        "answer_hash": "7b681f62cc828c6d7568ef7f3a350428",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "F",
        "variable_idxs": (0, 1),
        "str_func": float_to_str,
        "answer_hash": "ff917d13cdf6acdd0e17a176a570963e",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "F",
        "variable_idxs": (0, 2),
        "str_func": float_to_str,
        "answer_hash": "d950e2cbd82caf777485907cf003584f",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "F",
        "variable_idxs": (0, 3),
        "str_func": float_to_str,
        "answer_hash": "02c733f0fdc78a155bafe8d953cb95d7",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "F",
        "variable_idxs": (1, 0),
        "str_func": float_to_str,
        "answer_hash": "9af9af4c7374f0b14fafa874d5bd003f",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "F",
        "variable_idxs": (1, 1),
        "str_func": float_to_str,
        "answer_hash": "b3642522f0ba3e96b095f1b16f4c4eca",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "F",
        "variable_idxs": (1, 2),
        "str_func": float_to_str,
        "answer_hash": "dd0580ff997a6c0ff5b0c5c026844ab0",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "F",
        "variable_idxs": (1, 3),
        "str_func": float_to_str,
        "answer_hash": "044e197410340e5ff6f33350b73d1e89",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "F",
        "variable_idxs": (2, 0),
        "str_func": float_to_str,
        "answer_hash": "c23fe4bb535bac9d90c828dc3717e93b",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "F",
        "variable_idxs": (2, 1),
        "str_func": float_to_str,
        "answer_hash": "ac45c1a4dc7225534e911394e1370aea",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "F",
        "variable_idxs": (2, 2),
        "str_func": float_to_str,
        "answer_hash": "28d810834d62455e7520b5e6e2990437",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "F",
        "variable_idxs": (2, 3),
        "str_func": float_to_str,
        "answer_hash": "216542c4e092b5267c050babc85adf9d",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "F",
        "variable_idxs": (3, 0),
        "str_func": float_to_str,
        "answer_hash": "1b1241ecfc9d00dd5c3bcb35ea370abf",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "F",
        "variable_idxs": (3, 1),
        "str_func": float_to_str,
        "answer_hash": "34a21d761f1b187400b73aabeb42c5bc",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "F",
        "variable_idxs": (3, 2),
        "str_func": float_to_str,
        "answer_hash": "b17f75679965dfecbb9f4d4f6b898309",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "F",
        "variable_idxs": (3, 3),
        "str_func": float_to_str,
        "answer_hash": "3b2a80974732efdab96fbb189d681695",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "Matrices_P",
        "variable_idxs": (0, 0),
        "str_func": float_to_str,
        "answer_hash": "3a7a6580a2f5bb09161b4057bf8c2ec1",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "Matrices_P",
        "variable_idxs": (0, 1),
        "str_func": float_to_str,
        "answer_hash": "1ee7efb648f980167d5b426e506c5e5b",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "Matrices_P",
        "variable_idxs": (0, 2),
        "str_func": float_to_str,
        "answer_hash": "cf22d8b0a0d84c7e7b938207426c5e9c",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "Matrices_P",
        "variable_idxs": (0, 3),
        "str_func": float_to_str,
        "answer_hash": "8760f75c6a0516216590c1c3ca83da84",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "Matrices_P",
        "variable_idxs": (1, 0),
        "str_func": float_to_str,
        "answer_hash": "36b51d06f92a9163470007baf5a10563",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "Matrices_P",
        "variable_idxs": (1, 1),
        "str_func": float_to_str,
        "answer_hash": "0912da826812d262182bc33c2c90ec4b",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "Matrices_P",
        "variable_idxs": (1, 2),
        "str_func": float_to_str,
        "answer_hash": "162ef2da202807abbc1556998d7f7704",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "Matrices_P",
        "variable_idxs": (1, 3),
        "str_func": float_to_str,
        "answer_hash": "e1036d685ce8c4d8f456e61a27974666",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "Matrices_P",
        "variable_idxs": (2, 0),
        "str_func": float_to_str,
        "answer_hash": "706ac89b0d33b893f754e65d4acb52de",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "Matrices_P",
        "variable_idxs": (2, 1),
        "str_func": float_to_str,
        "answer_hash": "92f97f3c6af5bacfef7c456cf38768ba",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "Matrices_P",
        "variable_idxs": (2, 2),
        "str_func": float_to_str,
        "answer_hash": "aadd46e4fcc00613efc41fc1dd2c4076",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "Matrices_P",
        "variable_idxs": (2, 3),
        "str_func": float_to_str,
        "answer_hash": "01130a22727aa7093fd51789eca6b022",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "Matrices_P",
        "variable_idxs": (3, 0),
        "str_func": float_to_str,
        "answer_hash": "3787511c101639cfea71dc055636210c",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "Matrices_P",
        "variable_idxs": (3, 1),
        "str_func": float_to_str,
        "answer_hash": "e915c6f9fbe1e210f6f5ab6972bac153",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "Matrices_P",
        "variable_idxs": (3, 2),
        "str_func": float_to_str,
        "answer_hash": "c1545b16b9d69ee83b30124c6ffddcf1",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "Matrices_P",
        "variable_idxs": (3, 3),
        "str_func": float_to_str,
        "answer_hash": "9ae3a299b00c00281f9a0e5a7c6159df",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "Matrices_F",
        "variable_idxs": (0, 0),
        "str_func": float_to_str,
        "answer_hash": "b4936fdfbe2038c4e8bb14112b118cf7",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "Matrices_F",
        "variable_idxs": (0, 1),
        "str_func": float_to_str,
        "answer_hash": "a92074802ec38f8634db12e85991766d",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "Matrices_F",
        "variable_idxs": (0, 2),
        "str_func": float_to_str,
        "answer_hash": "36531034cdf99c39a82d4db374afd26b",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "Matrices_F",
        "variable_idxs": (0, 3),
        "str_func": float_to_str,
        "answer_hash": "ec39ccfce4d82d444c281b0fd9b3629b",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "Matrices_F",
        "variable_idxs": (1, 0),
        "str_func": float_to_str,
        "answer_hash": "76fbdc8ddb0567fe6f2286bdb350aa5e",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "Matrices_F",
        "variable_idxs": (1, 1),
        "str_func": float_to_str,
        "answer_hash": "3b2d29301c418594aee149a6a09f5378",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "Matrices_F",
        "variable_idxs": (1, 2),
        "str_func": float_to_str,
        "answer_hash": "1f6f62ec939d2667aedd7c61d2fe1718",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "Matrices_F",
        "variable_idxs": (1, 3),
        "str_func": float_to_str,
        "answer_hash": "21b3d0ab787d745a39852a5b7adb739f",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "Matrices_F",
        "variable_idxs": (2, 0),
        "str_func": float_to_str,
        "answer_hash": "1782be29eef86f321ed17f412ed61688",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "Matrices_F",
        "variable_idxs": (2, 1),
        "str_func": float_to_str,
        "answer_hash": "6bfb14bb97f217616c76cecd6603d14b",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "Matrices_F",
        "variable_idxs": (2, 2),
        "str_func": float_to_str,
        "answer_hash": "e8be0bea4b8a5514c325006ccb8f1cb0",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "Matrices_F",
        "variable_idxs": (2, 3),
        "str_func": float_to_str,
        "answer_hash": "08e6e70b73b0d5bff020d9c7dd0c3328",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "Matrices_F",
        "variable_idxs": (3, 0),
        "str_func": float_to_str,
        "answer_hash": "9ba43f2445c77d6a051ac73eb6225525",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "Matrices_F",
        "variable_idxs": (3, 1),
        "str_func": float_to_str,
        "answer_hash": "22abdaf6b9900e3fdcda70f62c93736b",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "Matrices_F",
        "variable_idxs": (3, 2),
        "str_func": float_to_str,
        "answer_hash": "30e4cfd5cc4ad93d3a91936c44b98573",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "Matrices_F",
        "variable_idxs": (3, 3),
        "str_func": float_to_str,
        "answer_hash": "fdce1125b7f3004466b23041a155c6c8",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "Matrices_H",
        "variable_idxs": (0, 0),
        "str_func": float_to_str,
        "answer_hash": "74ceb436e958faa430acada60dbb01c2",
        "points_avail": 1.0 / 8.0,
    },
    {
        "variable_name": "Matrices_H",
        "variable_idxs": (0, 1),
        "str_func": float_to_str,
        "answer_hash": "bb16bfa13304dfe3f96e04f852e8153c",
        "points_avail": 1.0 / 8.0,
    },
    {
        "variable_name": "Matrices_H",
        "variable_idxs": (0, 2),
        "str_func": float_to_str,
        "answer_hash": "d4319c9db61c76d4805357ad9da61ecb",
        "points_avail": 1.0 / 8.0,
    },
    {
        "variable_name": "Matrices_H",
        "variable_idxs": (0, 3),
        "str_func": float_to_str,
        "answer_hash": "4f2a6f99265eb51334385ebaf1932a43",
        "points_avail": 1.0 / 8.0,
    },
    {
        "variable_name": "Matrices_H",
        "variable_idxs": (1, 0),
        "str_func": float_to_str,
        "answer_hash": "06390f337ee1307f64c1b73fc1dd8f8d",
        "points_avail": 1.0 / 8.0,
    },
    {
        "variable_name": "Matrices_H",
        "variable_idxs": (1, 1),
        "str_func": float_to_str,
        "answer_hash": "5982f8640d6dbfffd76a5c207bfeb6d5",
        "points_avail": 1.0 / 8.0,
    },
    {
        "variable_name": "Matrices_H",
        "variable_idxs": (1, 2),
        "str_func": float_to_str,
        "answer_hash": "4f8d99e4aa45d6691276bbf514180e1a",
        "points_avail": 1.0 / 8.0,
    },
    {
        "variable_name": "Matrices_H",
        "variable_idxs": (1, 3),
        "str_func": float_to_str,
        "answer_hash": "9a6fbd59d0109625d271ae6292fd0927",
        "points_avail": 1.0 / 8.0,
    },
    {
        "variable_name": "Matrices_R",
        "variable_idxs": (0, 0),
        "str_func": float_to_str,
        "answer_hash": "03c032f83ce671a5513738c6a86a208d",
        "points_avail": 1.0 / 4.0,
    },
    {
        "variable_name": "Matrices_R",
        "variable_idxs": (0, 1),
        "str_func": float_to_str,
        "answer_hash": "3fe81ce3e8309b755ecd176ac15a7c69",
        "points_avail": 1.0 / 4.0,
    },
    {
        "variable_name": "Matrices_R",
        "variable_idxs": (1, 0),
        "str_func": float_to_str,
        "answer_hash": "4e4ebaaf63ea8286e63e23a5c0584376",
        "points_avail": 1.0 / 4.0,
    },
    {
        "variable_name": "Matrices_R",
        "variable_idxs": (1, 1),
        "str_func": float_to_str,
        "answer_hash": "9087f92b7c60ead8c8a8d15cb55d5c42",
        "points_avail": 1.0 / 4.0,
    },
    {
        "variable_name": "Matrices_I",
        "variable_idxs": (0, 0),
        "str_func": float_to_str,
        "answer_hash": "4e535f04c16bd34dc24b96a683bdd12f",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "Matrices_I",
        "variable_idxs": (0, 1),
        "str_func": float_to_str,
        "answer_hash": "5e705c24a37bcf684ee6654574e69817",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "Matrices_I",
        "variable_idxs": (0, 2),
        "str_func": float_to_str,
        "answer_hash": "69123f79dd97d11ad967ab2fc040ba86",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "Matrices_I",
        "variable_idxs": (0, 3),
        "str_func": float_to_str,
        "answer_hash": "cd402b6f495d92c79981b76c8f718f62",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "Matrices_I",
        "variable_idxs": (1, 0),
        "str_func": float_to_str,
        "answer_hash": "b2d08b094f666c9352522b410f262bd5",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "Matrices_I",
        "variable_idxs": (1, 1),
        "str_func": float_to_str,
        "answer_hash": "e4d42e5035083348a00e5aa369f10fab",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "Matrices_I",
        "variable_idxs": (1, 2),
        "str_func": float_to_str,
        "answer_hash": "2787eff86999f3f5ff895424a2fde7ae",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "Matrices_I",
        "variable_idxs": (1, 3),
        "str_func": float_to_str,
        "answer_hash": "3756917536cfb49c289a16d9f3027b0a",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "Matrices_I",
        "variable_idxs": (2, 0),
        "str_func": float_to_str,
        "answer_hash": "faf1c5b3c37f80173c0a9cf0bcdd8721",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "Matrices_I",
        "variable_idxs": (2, 1),
        "str_func": float_to_str,
        "answer_hash": "71457838393aae391cfa4dc47b726548",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "Matrices_I",
        "variable_idxs": (2, 2),
        "str_func": float_to_str,
        "answer_hash": "c6932c221e5267b703688bbe56647a11",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "Matrices_I",
        "variable_idxs": (2, 3),
        "str_func": float_to_str,
        "answer_hash": "160c4465ab27eecddb36ac8ffe05f0f5",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "Matrices_I",
        "variable_idxs": (3, 0),
        "str_func": float_to_str,
        "answer_hash": "7adfb0c92fc2deeeec7612a9dfcdeed2",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "Matrices_I",
        "variable_idxs": (3, 1),
        "str_func": float_to_str,
        "answer_hash": "c5cd88be595e5796feee90a5b1b4cf62",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "Matrices_I",
        "variable_idxs": (3, 2),
        "str_func": float_to_str,
        "answer_hash": "467eff2e5881cdedaddad426d6efeee8",
        "points_avail": 1.0 / 16.0,
    },
    {
        "variable_name": "Matrices_I",
        "variable_idxs": (3, 3),
        "str_func": float_to_str,
        "answer_hash": "b752232e68c33928284abfd5f76a14fa",
        "points_avail": 1.0 / 16.0,
    },
)

if __name__ == "__main__":
    checkutil.check(FILL_IN_TEST_CASES, (), locals())
