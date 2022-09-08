"""module sphere"""
import class_cercle

class Sphere(class_cercle.Cercle):
    """class sphere en detail"""
    def __init__(self, rayon: class_cercle.Number):
        super().__init__(rayon)

    def surface(self) -> float:
        return 0.0

def test_sphere():
    """test sphere"""
    s1 = Sphere(10)
    print(s1)
    print(f'{s1.surface() = }')

test_sphere()
