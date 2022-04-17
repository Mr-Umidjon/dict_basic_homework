def count_all(txt):
    """
    Return the result in a dictionary.
    Args:
        txt(str): count letters and digits
    Returns:
        dict: dictionary with letters and digits
    """
    res = {"LETTERS": 0, "DIGITS": 0}

    for i in txt:
        if i.isdigit():
            res['DIGITS'] += 1
        elif i.isalpha():
            res['LETTERS'] += 1
    return res
