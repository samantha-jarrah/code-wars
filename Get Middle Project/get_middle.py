import math


def get_middle(s):
    """
    Takes a string and returns the center character if string is of odd length and the 2 center characters if string
    is of even length.
    """
    if len(s) % 2 == 0:
        result = [s[int((len(s) / 2) - 1)], s[int((len(s) / 2))]]
        return "".join(result)
    else:
        return s[math.floor(len(s) / 2)]

