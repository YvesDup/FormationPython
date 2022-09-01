"""Class parallelo - exo20"""
import math
import sys


class Parallelo:
    """Class Parallelo - exo20"""
    def __init__(self, pc, gc, angle):
        for param in (pc, gc, angle):
            if not isinstance(param , (int, float)):
                raise TypeError(f'{param} doit être un entier ou un float')
        if not (0 < pc < gc):
            raise ValueError("0 < pc < gc n'est pas valide !!!")

        if not (45 <= angle <= 90):
            raise ValueError('angle doit etre compris entre 45 et 90')

        self.pc = pc 
        self.gc = gc
        self.angle = angle

    # formatage de chaine 
    def __str__(self) -> str:
        return f"str {hex(id(self))}"

    def __repr__(self) -> str:
        return f"repr {hex(id(self))}"

    # opertauer de comparaison
    def __eq__(self, other) -> bool:
        return self.pc == other.pc\
            and self.gc == other.gc\
            and self.angle == other.angle

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    # fonctionel
    def perimetre(self) -> float:
        return 2 * (self.pc + self.gc)

    def surface(self) -> float:
        return self.pc * self.gc * math.sin(math.radians(self.angle))

def test_parallelo():
    """fonction de test"""
    try:
        p = Parallelo(10, 20)
    except Exception as e :
        print(e)

    try:
        p = Parallelo(10, 20, 30, 40)
    except Exception as e :
        print(e)

    try:
        p = Parallelo(10, 20, 90)
        print(p, "surface = ",p.surface(), "perimetre = ", p.perimetre())
    except Exception as e :
        print(e)

    print(f"{p == Parallelo(10, 20, 60) = }")

if __name__ == "__main__":
    print(sys.version)
    test_parallelo()