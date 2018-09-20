def mult_lists(a, b):
    """
    >>> mult_lists([1, 1], [1, 1])
    2
    >>> mult_lists([1, 2], [1, 4])
    9
    >>> mult_lists([1, 2, 1], [1, 4, 3])
    12
    """
    n = 0
    result = 0
    for index in range(len(a)):
        result = result + (a[n] * b[n])
        n = n+1
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
