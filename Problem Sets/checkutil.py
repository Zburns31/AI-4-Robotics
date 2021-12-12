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

from __future__ import division
from __future__ import print_function

from io import StringIO
from builtins import str
import sys

import hashlib
import traceback

float_to_str = lambda x: "%.04f" % x
do_nothing = lambda x: x


# helper function for fillin matrix
def get_indexed(x, idxs):
    ret = x
    for idx in idxs:
        ret = ret[idx]
    return ret


def format_2d_arr(p):
    try:
        rows = ['[' + ','.join(['{0:.5f}'.format(x) for x in r]) + ']' for r in p]
        return '[' + ',\n '.join(rows) + ']'
    except Exception as e:
        return str(p)


def array_size(arr):
    try:
        h = len(arr)
        w = len(arr[0])
        return (h, w)
    except Exception as e:
        return (0, 0)


def arrays_approx_equal(arr0, arr1, epsilon=0.001):
    size0 = array_size(arr0)
    size1 = array_size(arr1)

    if size0 != size1:
        return False

    rows, cols = size0

    for i in range(rows):
        for j in range(cols):
            if abs(arr0[i][j] - arr1[i][j]) > epsilon:
                return False

    return True


def generate_answer_hash(variable_name, variable_idxs=(), value_str=''):
    s = '%s_%s_%s' % (variable_name,
                      ','.join([str(idx) for idx in variable_idxs]),
                      value_str)
    return hashlib.md5(s.encode('utf8')).hexdigest()


def get_global_value(name, extra_context=None, defval=None):
    if name in globals():
        return globals()[name]
    elif extra_context and name in extra_context:
        return extra_context[name]
    else:
        return defval


def check_fill_in_test_case(variable_name,
                            str_func,
                            answer_hash,
                            points_avail=1,
                            variable_idxs=(),
                            extra_context=None):
    """
    Generic function for checking fill-in answers.

    :return: a tuple (earned, avail, msg) tuple
    """

    result = ''
    points_earned = 0

    source = None
    if variable_name in globals():
        source = globals()
    elif extra_context is not None and variable_name in extra_context:
        source = extra_context

    if source:
        try:
            value = str_func(get_indexed(source[variable_name], variable_idxs))
        except Exception as e:
            value = ''

        value_hash = generate_answer_hash(variable_name, variable_idxs, value)
        points_earned = points_avail if value_hash == answer_hash else 0
        ind = 'ind: ' + str(variable_idxs) + ' ' if len(variable_idxs) > 0 else ''
        result = ind + '<OK>' if points_earned else ind + '<INCORRECT>'

    else:
        result = 'variable not defined'

    display_info = (variable_name, result, round(points_earned, 3), round(points_avail, 3))
    return points_earned, points_avail, display_info


def check_code_test_case(function_name,
                         function_input,
                         expected_output,
                         outputs_match_func,
                         output_to_str_func,
                         points_avail=1,
                         tries=1,
                         matches_required=1,
                         extra_context=None):
    detailed_results = '\n'
    error_msg = ''
    points_earned = 0

    source = None
    if function_name in globals():
        source = globals()
    elif extra_context is not None and function_name in extra_context:
        source = extra_context

    if source:
        old_stdout = sys.stdout
        sys.stdout = capture_io = StringIO()
        matches = ()

        for t in range(1, tries + 1):

            try:
                output = source[function_name](**function_input)
                outputs_match = outputs_match_func(output, expected_output)
            except Exception as e:
                output = None
                outputs_match = False
                error_msg = str(e) + traceback.format_exc()

            matches += (outputs_match,)

            if outputs_match:

                detailed_results += 'attempt %02d: correct\n' % t

            else:

                detailed_results += "attempt %02d: output does not match expected\n" % t
                detailed_results += " " * 12 + "actual:   "

                try:
                    detailed_results += output_to_str_func(output) + "\n"
                except Exception as e:
                    detailed_results += str(output) + "\n"

                detailed_results += " " * 12 + "expected: "

                try:
                    detailed_results += output_to_str_func(expected_output) + "\n"
                except Exception as e:
                    detailed_results += str(expected_output) + "\n"

                if error_msg:
                    detailed_results += "error msg: " + error_msg + "\n"

        sys.stdout = old_stdout
        printed_output = capture_io.getvalue()
        if printed_output != '':
            detailed_results += f' ~~~ print() output <start> ~~~\n'
            detailed_results += printed_output
            detailed_results += f' ~~~ print() output   <end> ~~~\n'
        detailed_results = detailed_results\
            .replace('\n','\n  |').rstrip(' |').lstrip('\n')\
            .replace('  ', "  " if 'ps' in sys.argv[0] else " `")

        total_matches = sum([1 for m in matches if m])
        if total_matches >= matches_required:
            points_earned = points_avail
            outcome = f'<OK> {total_matches} ({matches_required} to pass)'
        else:
            outcome = f'<INCORRECT> {total_matches} ({matches_required} to pass)'

    else:
        outcome = 'function not defined'

    display_info = (
        f'{function_name} ({tries} tr{"y" if tries == 1 else "ies"})',
        outcome,
        round(points_earned, 3),
        round(points_avail, 3)
    )

    return points_earned, points_avail, display_info, detailed_results


def check(fill_in_test_cases=(),
          code_test_cases=(),
          extra_context=None):
    MAX_COL_WIDTH = 25
    HEADER_NAMES = [[
        'Problem Name',
        'Result',
        'Credit',
        'Possible',
    ]]
    earned_total = 0
    avail_total = 0
    loginid = get_global_value('whoami',
                               extra_context=extra_context,
                               defval='')
    if loginid:
        print("whoami: ", loginid)
        problem_results = []
        for test_case in fill_in_test_cases:
            earned, avail, display_info = check_fill_in_test_case(extra_context=extra_context,
                                                                  **test_case)
            earned_total += earned
            avail_total += avail
            problem_results.append(display_info)

        problem_details = []
        for test_case in code_test_cases:
            earned, avail, display_info, detailed_results = check_code_test_case(extra_context=extra_context,
                                                                                 **test_case)
            earned_total += earned
            avail_total += avail
            problem_results.append(display_info)
            problem_details.append(detailed_results)
        
        total_earned = round(earned_total, 3)
        total_possible = round(sum(map(lambda t: t[3], problem_results)))
        total_percent = int((total_earned * 100.0) / total_possible)
        final_results = [('TOTAL', f'{total_percent}%', total_earned, total_possible)]
        
        max_widths = []
        col_lst = list(zip(*(HEADER_NAMES + problem_results)))
        for col_values in col_lst:
            max_widths.append(max(map(lambda i: min(len(str(i)), MAX_COL_WIDTH), col_values)))
        horizontal_separator = [['=' * m for m in max_widths]]
        for row in horizontal_separator + \
                    HEADER_NAMES + \
                    horizontal_separator + \
                    problem_results + \
                    horizontal_separator + \
                    final_results + \
                    horizontal_separator:
            problem_name, result, points_earned, points_avail = row
            print(
                f'| {problem_name.ljust(max_widths[0])[:MAX_COL_WIDTH]} | '
                f'{result.ljust(max_widths[1])[:MAX_COL_WIDTH]} | '
                f'{str(points_earned).ljust(5, " ").center(max_widths[2])[:MAX_COL_WIDTH]} | '
                f'{str(points_avail).ljust(5, " ").center(max_widths[3])[:MAX_COL_WIDTH]} |'
                    .replace(' ', '=' if '=' in result else ' ')
                    .replace('  ', "  " if 'ps' in sys.argv[0] else " `")
            )
        print('\nExtra Info:')
        for problem, details in zip(col_lst[0][len(fill_in_test_cases)+1:], problem_details):
            print(problem)
            print(details)
        print(f'Score: {total_percent}')
    else:
        print("Student ID not specified.  Please fill in 'whoami' variable.")
        print(f'Score: 0')


def print_if_exists(label, value):
    if value:
        print(label + '\n' + value + '\n')
