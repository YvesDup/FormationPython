"""La sphere"""
import math

import class_cercle

class Sphere(class_cercle.Cercle):
    """class Sphere"""
    def __init__(self, rayon: class_cercle.Number):
        super().__init__(rayon)

    def surface(self) -> float:
        return 4 * self._rayon**2 * math.pi 

def test_sphere():
    """rrr
    """
    s1 =Sphere(100)
    print(s1)
    print(f'{s1.perimetre() = } - {s1.surface() = }')


test_sphere()
