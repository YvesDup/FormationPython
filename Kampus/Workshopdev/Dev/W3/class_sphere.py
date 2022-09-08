"""module sphere"""
import cercle

class Sphere(cercle.Cercle):
    """class sphere en detail"""
    def __init__(self, rayon: cercle.Number):
        super().__init__(rayon)

    def surface(self) -> float:
        return 0.0

def test_sphere():
    """test sphere"""
    s1 = Sphere(10)
    print(s1)

test_sphere()
