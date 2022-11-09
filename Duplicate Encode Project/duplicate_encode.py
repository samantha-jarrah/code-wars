def duplicate_encode(word):
    """
    Returns a new string containing a ( for each unique character in a string and ) for repeated characters.  It is not
    case specific.
     """
    new_string = []
    word = word.lower()
    for char in word:
        equal = False
        for index in range(word.index(char) + 1, len(word)):
            if char == word[index]:
                equal = True
        if equal == False:
            new_string.append("(")
        else:
            new_string.append(")")
            equal = False

    joined_string = "".join(new_string)
    return joined_string

