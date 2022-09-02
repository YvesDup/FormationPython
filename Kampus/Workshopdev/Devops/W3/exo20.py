import math
import sys


class Parallelo:

    def __init__(self, p_cote, g_cote, angle):
        # controle sur les types entrants
        for param in (p_cote, g_cote, angle):
            if not isinstance(param, (int, float)):
                raise TypeError(f"{param!r} doit être un entier ou un réel !!")

        # controle sur les valeurs admises
        if not (0 < p_cote < g_cote):
            raise ValueError("petit cote doit etre positif et plus petit que grand coté !!")

        if not ( 45 < angle <= 90):
            raise ValueError("Angle entre 45 et 90 ° compris")

        self.p_cote = p_cote
        self.g_cote = g_cote
        self 
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
    jeux_essais_init = (
                (10, 10, "10"),
                (10, "20", 10),
                ("5", 20, 40),
                (30, 20, 15),
                (-10, 10, 20),
                (10, -30, 20),
                (10, 76, 112),
                )
    for pc, gc, angle in jeux_essais_init:
        try:
            t = Parallelo(pc, gc, angle)
        except (TypeError, ValueError) as e:
            print(e)
        else:
            print(pc, gc, angle, "ne plante pas")

    print(t.poly(1))

if __name__ == "__main__":
    print(sys.version)
    test_parellelo() 