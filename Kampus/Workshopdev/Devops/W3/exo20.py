import math
import sys


class Parallelo:

    def __init__(self, p_cote, g_cote, angle):
        for param in (p_cote, g_cote, angle):
            if not isinstance(param, (int, float)):
                raise TypeError("param doit être un entier ou un réel !!")

    # conversion en string
    def __str__(self) -> str:
        return "STR"

    def __repr__(self) -> str:
        return "REPR"

    # metodes fonctionnelles
    def perimetre(self) -> float:
        return 0.0

    def surface(self) -> float:
        """math.radians(degrees) convertit un angfle en degre vers du radians
        math.son(angle_en_radians) ..."""
        return 0.0

    def poly(self, x, y):
        return "poly1"

    def poly(self, z):
        return "poly2"

def test_parellelo():
    """Test la classe Pärallelo"""

    t = Parallelo(10)
    print(t.poly(1))

if __name__ == "__main__":
    print(sys.version)
    test_parellelo() 