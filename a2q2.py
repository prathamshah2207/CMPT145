###############################################################################
# CMPT 145 Course material
# Original Author: Lauresa Stilling
# Date Created:   31 May 2023
# Last Edited:    31 May 2023
#
# All rights reserved.
#
# This document contains resources for homework assigned to students of
# CMPT 145 and shall not be distributed without permission.  Posting this
# file to a public or private website, or providing this file to a person
# not registered in CMPT 145, constitutes Academic Misconduct, according
# to the University of Saskatchewan Policy on Academic Misconduct.
#
# Synopsis:
#    Testing; relevant to Chapter 5, 6, 7
###############################################################################

# TODO: Fill in your information below
# Student Name
# NSID
# Student Number

################### DO NOT ALTER CODE BELOW ###################################
def gcd(val1: int, val2: int) -> int:
    """
    Purpose: Find the greatest common divisor (gcd) of the two values passed in.
    Pre-conditions:
        :param val1: int - integer value being compared to find gcd.
            Must be less than 1000, else returns -1
        :param val2: int - integer value being compared to find gcd
            Must be less than 1000, else returns -1
    Post Conditions:
        None
    Return:
        int - The greatest common positive divisor of the two numbers passed in.
            -1 returned on failure.
    """
    return -1


def replace(input_str: str, target: str, replacement: str) -> str:
    """
    Purpose: Replace all instances of target string with replacement string within input string.
        Starting at the first occurrence of target string.
    Pre-condition
        :param input_str:str - input string to change target strings to replacement strings
        :param target: str - string that one wishes to change
        :param replacement: str - string that will replace target strings in the input string
    Post Condition:
        None
    Return:
        str - new string where target strings have been changed to replacement string
    """
    new_str = ""
    inp_len = len(input_str)
    targ_len = len(target)
    if inp_len < targ_len:
        new_str = input_str
    else:
        i = 0
        while i < inp_len:
            if input_str[i:i+targ_len] == target:
                new_str += replacement
                i += targ_len
            else:
                new_str += input_str[i]
                i += 1
    return new_str


def grade_letter(score:int) -> str:
    """
    Purpose: Get the grade letter related to the score passed in.

    Pre-condition
        :param score:int - the number being calculated to a letter grade.
            Should be within the range of 0-100
    Post Condition:
        None
    Return:
        str - string associated with the score passed in
            if score is outside valid range returns the string "Invalid"
    """
    letter = ""
    if score < 0 or score > 100:
        letter = "Invalid"
    elif score >= 90:
        letter = "A"
    elif score >= 80:
        letter = "B"
    elif score >= 70:
        letter = "C"
    elif score >= 60:
        letter = "D"
    else:
        letter = "F"
    return letter

def sort_students_into_grades(student_list: list) -> dict:
    """
    Purpose: Goes through a list of dictionaries adding student names to the appropriate dictionary grade letter
        If the student's grade is not one of "A", "B", "C", "D", or "F", it is added to list "Invalid".
    Pre-condition:
        :param student_list: list of dictionaries,
            each dictionary represents a student and contains two keys: 'name' and 'grade'
    Post Condition:
        None
    Return:
        dict with lists as values; each key has a list value of names of students with that grade letter.
            Contains the keys "A","B","C","D","F","Invalid"
    """
    return {}
################### DO NOT ALTER CODE ABOVE ###################################


# TODO: Create tests for functions above
# TODO Create test driver for whitebox tested functions
# TODO: Create test driver for blackbox tested functions
# TODO: Create test driver to test all functions

