"""Class parallelo - exo20"""
import math
import sys
from xml.dom.pulldom import parseString


class Parallelo:
    """Class Parallelo - exo20"""
    def __init__(self, pc, gc, angle):
        pass

    def __str__(self) -> str:
        return ""

    def __repr__(self) -> str:
        return ""

    def perimetre(self) -> float:
        return 0.0

    def surface(self) -> float:
        return 0.0

def test_parallelo():
    """fonction de test"""
    try:
        p = parallelo(10, 20, 60)
        print(p, p.surface(), p.surface())
    except:
        parseString