def digital_root(n):
    """Takes an integer and successively adds its individual digits until it receives a single integer. """
    while n > 9:
        num_list = [int(x) for x in str(n)]
        n = 0
        for item in num_list:
            n += item
    return n

