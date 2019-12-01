def test(x):
    """>>> test(1)
    5"""
    print(x**4 +  4**x)
import doctest
doctest.testmod()
