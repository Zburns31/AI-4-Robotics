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
#       python ps0_answers.py
#
######################################################################

# If you see different scores locally and on Gradescope this may be an indication
# that you are uploading a different file than the one you are executing locally.
# If this local ID doesn't match the ID on Gradescope then you uploaded a different file.

OUTPUT_UNIQUE_FILE_ID = False
if OUTPUT_UNIQUE_FILE_ID:
    import hashlib, pathlib
    file_hash = hashlib.md5(pathlib.Path(__file__).read_bytes()).hexdigest()
    print(f'Unique file ID: {file_hash}')

# STUDENT ID
#
# Please specify your GT login ID in the whoami variable (ex: jsmith321).
#
whoami = ''


# Question 1: Bank account balance
class Question1:
    def __init__(self):
        """
        Initialize the account balance to zero.
        """

    def deposit(self, amount):
        """
        :param amount: the amount to be added to the existing balance
        :return: None
        """

    def withdraw(self, amount):
        """

        :param amount: the amount to be removed from the existing balance
        :return: None
        """

    def get_balance(self):
        """
        :return: the balance
        """


# Question 2: Bank account: dimes and quarters (dictionary)
class Question2:
    def __init__(self, dimes_and_quarters=None):
        """
        Initialize the number of dimes and quarters to the provided numbers. A dime is equal to 10-cents, i.e.,
        $ 0.10, whereas a quarter is equal 25-cents, i.e., $ 0.25. :param dimes_and_quarters: a optional dictionary
        containing the initial number of dimes and quarters, with the keys 'dimes' and/or 'quarters', eg: {'dimes':
        5, 'quarters': 10}. Note that the input parameter dimes_and_quarters can contain zero, one or two keys from
        'dimes' and 'quarters'. If a key is not provided in the input parameter dimes_and_quarters, initialize its
        value to zero.

            Example value: dimes_and_quarters = {'dimes': 5, 'quarters': 10} means that we are starting with 5 dimes
            and 10 quarters. Another example value: dimes_and_quarters = {'quarters': 10} means that we are starting
            with no dimes and 10 quarters. Another example value: dimes_and_quarters = {} or dimes_and_quarters =
            None means that we are starting with 0 dimes and 0 quarters.
        """

    def add_coins(self, dimes_and_quarters):
        """
        :param dimes_and_quarters: a dictionary containing the number of dimes and quarters to be added,
        with the keys 'dimes' and/or 'quarters', eg: {'dimes': 5, 'quarters': 10}. Note that the input parameter
        dimes_and_quarters can contain zero, one or two keys from 'dimes' and 'quarters'. If a key is not provided in
        the input parameter dimes_and_quarters, that means the coins of that type are not added, i.e., consider the
        number of that type of coins to be added as zero.

                Example value: dimes_and_quarters = {'dimes': 5, 'quarters': 10} means that we are adding with 5
                dimes and 10 quarters. Another example value: dimes_and_quarters = {'quarters': 10} means that we are
                adding 0 dimes and 10 quarters. Another example value: dimes_and_quarters = {} means that we are not
                adding any dimes or quarters. :return: None
        """

    def remove_coins(self, dimes_and_quarters):
        """

        :param dimes_and_quarters: a dictionary containing the number of dimes and quarters to be removed,
        with the keys 'dimes' and/or 'quarters', eg: {'dimes': 5, 'quarters': 10}. Note that the input parameter
        dimes_and_quarters can contain zero, one or two keys from 'dimes' and 'quarters'. If a key is not provided in
        the input parameter dimes_and_quarters, that means the coins of that type are not removed, i.e., consider the
        number of that type of coins to be removed as zero.

                Example value: dimes_and_quarters = {'dimes': 5, 'quarters': 10} means that we are removing with 5
                dimes and 10 quarters. Another example value: dimes_and_quarters = {'quarters': 10} means that we are
                removing 0 dimes and 10 quarters. Another example value: dimes_and_quarters = {} means that we are
                not removing any dimes or quarters. :return: None
        """

    def get_coins(self):
        """
        :return: dimes and quarters collected till now in a dictionary of the form eg: {'dimes': 5, 'quarters': 10}.
        Note that the output dictionary needs to have both the keys. If suppose the quarters are zero and dimes are
        2, the return value should be {'dimes': 2, 'quarters': 0}.
        """

    def get_balance_cents(self):
        """
        :return: the balance amount (in cents), taking into account the value of each type of coin. Eg: if we have 5
        dimes and 2 quarters in the balance, then the return value should be 5 * 10 + 2 * 25 = 100.
        """


# Question 3: Bank account: dimes and quarters (tuple)
class Question3:
    def __init__(self, dimes_and_quarters=None):
        """
        Initialize the number of dimes and quarters to the provided numbers. A dime is equal to 10-cents, i.e.,
        $ 0.10, whereas a quarter is equal 25-cents, i.e., $ 0.25. :param dimes_and_quarters: a optional dictionary
        containing the initial number of dimes and quarters, with the keys 'dimes' and/or 'quarters', eg: {'dimes':
        5, 'quarters': 10}. Note that the input parameter dimes_and_quarters can contain zero, one or two keys from
        'dimes' and 'quarters'. If a key is not provided in the input parameter dimes_and_quarters, initialize its
        value to zero.

            Example value: dimes_and_quarters = {'dimes': 5, 'quarters': 10} means that we are starting with 5 dimes
            and 10 quarters. Another example value: dimes_and_quarters = {'quarters': 10} means that we are starting
            with no dimes and 10 quarters. Another example value: dimes_and_quarters = {} or dimes_and_quarters =
            None means that we are starting with 0 dimes and 0 quarters.
        """

    def add_coins(self, dimes_and_quarters):
        """
        :param dimes_and_quarters: a tuple of the number of dimes and quarters to be added to the existing list of
        coins. This will always be a tuple of exactly two numbers, (dimes and quarters respectively). Example value:
        dimes_and_quarters = (5, 6) means that there are 5 dimes and 6 quarters to be added. Another Example value:
        dimes_and_quarters = (5, 0) means that there are 5 dimes and no quarters to be added. :return: None
        """

    def remove_coins(self, dimes_and_quarters):
        """

        :param dimes_and_quarters: a tuple of the number of dimes and quarters to be removed from the existing list
        of coins. This will always be a tuple of exactly two numbers, (dimes and quarters respectively). Example
        value: dimes_and_quarters = (5, 6) means that there are 5 dimes and 6 quarters to be removed. Another Example
        value: dimes_and_quarters = (0, 5) means that there are no dimes and 5 quarters to be removed. :return: None
        """

    def get_balance_cents(self):
        """
        :return: the balance amount (in cents), taking into account the value of each type of coin. Eg: if we have 5
        dimes and 2 quarters in the balance, then the return value should be 5 * 10 + 2 * 25 = 100.
        """


# Question 4: Debugging
class Question4:
    # Identify and fix the errors
    def __init__(self, accounts):
        """
        :param accounts: contains accounts of multiple people of the form {'CustomerName': [dimes, quarters]} . Eg
        value: { 'Alex': (5, 10), 'Bob': (0, 2) }
        """
        self.accounts = accounts

    def display_balance(self):
        """
        You have to make a minor change to get rid of the error.
        :return: balance string: Expected output example: (Customer: Alex, Balance: 300)(Customer: Bob, Balance: 50)
        """
        output = ''
        for customer_name, account_info in self.accounts.items():
            customer_name, dimes, quarters = account_info
            balance = dimes * 10 + quarters * 25
            output = output + f'(Customer: {customer_name}, Balance: {balance})'
        return output


######################################################################
# Grading methods
#
# Do not modify code below this point.
#
# The auto-grader does not use any of the below code
#
######################################################################
import copy
import traceback

FILL_IN_TEST_CASES = ({})  # empty dictionary; no such questions in ps0


def q1_check(functions, arguments):
    student_output = []
    try:
        account = Question1()
        method_mapping = {'getBalance': account.get_balance, 'deposit': account.deposit, 'withdraw': account.withdraw}
        for function, argument in zip(functions, arguments):
            student_output.append(_run_method(function, method_mapping, argument))
    except Exception as e:
        print(traceback.format_exc())
    return student_output


def q2_check(functions, arguments):
    student_output = []
    try:
        account = Question2()
        method_mapping = {'__init__': account.__init__, 'addCoins': account.add_coins,
                          'removeCoins': account.remove_coins, 'getBalanceCents': account.get_balance_cents,
                          'getCoins': account.get_coins}
        for function, argument in zip(functions, arguments):
            student_output.append(_run_method(function, method_mapping, argument))
    except Exception as e:
        print(traceback.format_exc())
    return student_output


def q3_check(functions, arguments):
    student_output = []
    try:
        account = Question3()
        method_mapping = {'__init__': account.__init__, 'addCoins': account.add_coins,
                          'removeCoins': account.remove_coins, 'getBalanceCents': account.get_balance_cents}
        for function, argument in zip(functions, arguments):
            student_output.append(_run_method(function, method_mapping, argument))
    except Exception as e:
        print(traceback.format_exc())
    return student_output


def q4_check(functions, arguments):
    student_output = []
    try:
        account = Question4(arguments[0])  # implicitly assume first call is always to init, with appropriate parameter
        student_output.append(None)
        method_mapping = {'displayBalance': account.display_balance}
        for function, argument in zip(functions[1:], arguments[1:]):
            student_output.append(_run_method(function, method_mapping, argument))
    except Exception as e:
        print(traceback.format_exc())
    return student_output


def _run_method(function, method_mapping, argument):
    if argument is not None:
        ret_val = copy.deepcopy(method_mapping[function](argument))
    else:
        ret_val = copy.deepcopy(method_mapping[function]())
    return ret_val


def compare_outputs(student_out, expected_out):
    test_result = True
    if len(student_out) != len(expected_out):
        test_result = False

    for i in range(len(student_out)):
        if student_out[i] != expected_out[i]:
            test_result = False

    return test_result


CODE_TEST_CASES = ({'function_name': 'q1_check',
                    'function_input': dict(functions=['getBalance', 'deposit', 'getBalance', 'deposit', 'getBalance',
                                                      'withdraw', 'getBalance', 'deposit', 'getBalance'],
                                           arguments=[None, 100, None, 20, None, 50, None, 20, None]),
                    'expected_output': [0, None, 100, None, 120, None, 70, None, 90],
                    'outputs_match_func': compare_outputs,
                    'output_to_str_func': str(),
                    'points_avail': 1},
                   {'function_name': 'q1_check',
                    'function_input': dict(
                        functions=['getBalance', 'deposit', 'getBalance', 'withdraw', 'getBalance', 'withdraw',
                                   'getBalance', 'deposit', 'getBalance'],
                        arguments=[None, 500, None, 20, None, 50, None, 20, None]),
                    'expected_output': [0, None, 500, None, 480, None, 430, None, 450],
                    'outputs_match_func': compare_outputs,
                    'output_to_str_func': str(),
                    'points_avail': 1},
                   {'function_name': 'q2_check',
                    'function_input': dict(
                        functions=['__init__', 'addCoins', 'getBalanceCents', 'getCoins', 'removeCoins', 'getCoins',
                                   'getBalanceCents'],
                        arguments=[{'dimes': 5}, {'dimes': 2, 'quarters': 10}, None, None,
                                   {'dimes': 2, 'quarters': 10}, None, None]),
                    'expected_output': [None, None, 320,  {'dimes': 7, 'quarters': 10}, None,
                                        {'dimes': 5, 'quarters': 0}, 50],
                    'outputs_match_func': compare_outputs,
                    'output_to_str_func': str(),
                    'points_avail': 1},
                   {'function_name': 'q2_check',
                    'function_input': dict(
                        functions=['__init__', 'getCoins', 'addCoins', 'getBalanceCents', 'getCoins', 'removeCoins',
                                   'getCoins', 'getBalanceCents'],
                        arguments=[{}, None, {'dimes': 20}, None, None, {'dimes': 5}, None, None]),
                    'expected_output': [None, {'dimes': 0, 'quarters': 0}, None, 200,  {'dimes': 20, 'quarters': 0},
                                        None, {'dimes': 15, 'quarters': 0}, 150],
                    'outputs_match_func': compare_outputs,
                    'output_to_str_func': str(),
                    'points_avail': 1},
                   {'function_name': 'q3_check',
                    'function_input': dict(
                        functions=['__init__', 'addCoins', 'getBalanceCents', 'removeCoins', 'getBalanceCents'],
                        arguments=[{'dimes': 5}, (2, 10), None, (2, 10), None]),
                    'expected_output': [None, None, 320, None, 50],
                    'outputs_match_func': compare_outputs,
                    'output_to_str_func': str(),
                    'points_avail': 1},
                   {'function_name': 'q3_check',
                    'function_input': dict(
                        functions=['__init__', 'addCoins', 'getBalanceCents', 'removeCoins', 'getBalanceCents',
                                   'addCoins', 'getBalanceCents'],
                        arguments=[{'dimes': 5, 'quarters': 1}, (2, 10), None, (2, 10), None, (0, 5), None]),
                    'expected_output': [None, None, 345, None, 75, None, 200],
                    'outputs_match_func': compare_outputs,
                    'output_to_str_func': str(),
                    'points_avail': 1},
                   {'function_name': 'q4_check',
                    'function_input': dict(
                        functions=['__init__', 'displayBalance'],
                        arguments=[{'Alex': (5, 10), 'Bob': (0, 2)}, None]),
                    'expected_output': [None, '(Customer: Alex, Balance: 300)(Customer: Bob, Balance: 50)'],
                    'outputs_match_func': compare_outputs,
                    'output_to_str_func': str(),
                    'points_avail': 1},
                   {'function_name': 'q4_check',
                    'function_input': dict(
                        functions=['__init__', 'displayBalance'],
                        arguments=[{'Alexa': (5, 10), 'Siri': (8, 2)}, None]),
                    'expected_output': [None, '(Customer: Alexa, Balance: 300)(Customer: Siri, Balance: 130)'],
                    'outputs_match_func': compare_outputs,
                    'output_to_str_func': str(),
                    'points_avail': 1}
                   )

if __name__ == '__main__':
    import checkutil
    checkutil.check(FILL_IN_TEST_CASES, CODE_TEST_CASES, locals())
