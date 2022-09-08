import sys

import exo20 as parallelo

class Losange(parallelo.Parallelo):
    """class Losange"""
    def __init__(self, cote, angle):
        pass

def test_losange():
    """
    """

class Rectange(parallelo.Parallelo):
    """"""
    def __init__(self, p_cote, g_cote):
        pass

def test_rectangle():
    """
    """

def test_all():
    """
    """
    r1 = Rectangle(10, 20)
    r2 = r1
    l1 = losange(100, 75)
    l = [Rectangle(30, 60), r1, l1, r2, Losange(10, 55)]
if __name__ == '__main__':
    print(sys.version)
    test_losange()
    test_rectangle()
