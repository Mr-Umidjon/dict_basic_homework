def create_dictionary(key, value):
    """
    Args:
        key(list): list of keys
        value(list): list of values
    Returns:
        dict: dictionary with keys and values
    """
    # res = {}
    # res.update(zip(key, value))
    # return res
    return dict(zip(key, value))


print(create_dictionary([1, 2, 3], ["one", "two", "three"]))
