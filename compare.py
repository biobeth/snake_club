def compare(a, b):
    """
    Returns 1 if a>b, 0 if a equals b, and -1 if a<b
    >>> compare(5, 4)
    1
    >>> compare(7,7)
    0
    >>> compare(2,3)
    -1
    >>> compare(42, 1)
    1
    """
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1


def hypotenuse (a, b):
    """
    compute the hypotenuse of a right triangle with sides of length a and b
    >>> hypotenuse(3, 4)
    5.0
    >>> hypotenuse(12, 5)
    13.0
    >>> hypotenuse(7, 24)
    25.0
    >>> hypotenuse(9, 12)
    15.0
    """
    C = (a**2) + (b**2)
    H = C**0.5
    return H


def fahrenheit_to_celsius(t):
    """
    >>> fahrenheit_to_celsius(212)
    100
    >>> fahrenheit_to_celsius(32)
    0
    >>> fahrenheit_to_celsius(-40)
    -40
    >>> fahrenheit_to_celsius(36)
    2
    >>> fahrenheit_to_celsius(37)
    3
    >>> fahrenheit_to_celsius(38)
    3
    >>> fahrenheit_to_celsius(39)
    4
    """
    T = (t-32)/1.8
    intT = round(T, 0)
    return int(intT)


    

