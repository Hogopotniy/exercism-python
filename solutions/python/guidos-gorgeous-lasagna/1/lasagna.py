"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO (student): define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40

PREPARATION_TIME_FOR_LAYER = 2


#TODO (student): Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """We take as an unput elapsed_bake_time and from constant need to minus to get remaing time
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


#TODO (student): Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.
def preparation_time_in_minutes(layers_num):
    """We take as an unput 'how many lawers' and then multiplying it to 'amount of minutes per 1 layer'
    """
    return layers_num * PREPARATION_TIME_FOR_LAYER


#TODO (student): define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(layers_num, elapsed_bake_time):
    """We take as an unput 'how many lawers' and EXPECTED_BAKE_TIME then sum total time
    """
    return elapsed_bake_time + preparation_time_in_minutes(layers_num)



# TODO (student): Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
