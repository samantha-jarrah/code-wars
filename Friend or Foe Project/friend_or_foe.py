def friend(x):
    """Takes a list of names and returns a new list containing only names with 4 letters"""
    friends = [name for name in x if len(name) == 4]
    return friends

