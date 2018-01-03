"""
    Parser.py contains the function parse_list_contents() and its auxiliary functions.
    This main function takes any  objects of type List  and parses all of the elements
    within it. Additionally,  the function can  recursively  parse the contents  of an
    element that is also of type List.

    Supported types: list, str, float, int
"""


def parse_list_contents(array):  # Recursively parses the contents of any multidimensional List, returns a new List
    if not isinstance(array, list):  # enforces List only policy
        raise TypeError("Function parameter must be a List")
    art = array[:]  # copies the array into art, preserving an original copy of the list
    for i in range(0, len(art)):  # iterates over the List's elements
        if isinstance(art[i], list):
            parse_list_contents(art[i])  # recursively parses an element of type List
        else:
            art[i] = __parse_numeric(art[i])  # parses non-list elements
    return art


def __parse_numeric(value):  # Attempts to parse a number, otherwise returns the original value
    if __contains(value, '.'):
        x = __parse_float(value)
    else:
        x = __parse_int(value)
    return x


def __parse_float(value):  # Attempts to parse a float, otherwise returns the original value
    try:
        x = float(value)
    except ValueError:
        x = value
    return x


def __parse_int(value):  # Attempts to parse an integer, otherwise returns the original value
    try:
        x = int(value)
    except ValueError:
        x = value
    return x


def __contains(string, char):  # Returns True if the given string contains the specified character
    contains = False
    for x in string:
        if x == char:
            contains = True
    return contains


"""
    Jan. 3 2:38PM CFigueroa
    Initial commit; includes parse_list_contents(), __parse_numeric(),
    __parse_float(), __parse_int() and __contains().
"""