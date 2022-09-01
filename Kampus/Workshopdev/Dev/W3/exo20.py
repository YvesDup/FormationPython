"""Class parallelo - exo20"""
import math
import sys


class Parallelo:
    """Class Parallelo - exo20"""
    def __init__(self, pc, gc, angle):
        if 
        if not (0 < pc < gc):
            return ValueError("0 < pc < gc n'est pas valide !!!")

            self.pc = pc 
            self.gc = gc
            self.angle = angle

    def __str__(self) -> str:
        return f"str {hex(id(self))}"

    def __repr__(self) -> str:
        return f"repr {hex(id(self))}"

    def perimetre(self) -> float:
        return 2 * (self.pc + self.gc)

    def surface(self) -> float:
        return 0.1

def test_parallelo():
    """fonction de test"""
    try:
        p = Parallelo(10, 20, 60)
        print(p, p.surface(), p.perimetre())
    except Exception as e :
        print(e)

if __name__ == "__main__":
    print(sys.version)
    test_parallelo()