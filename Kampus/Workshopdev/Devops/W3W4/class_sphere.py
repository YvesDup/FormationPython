import class_cercle

class Sphere(class_cercle.Cercle):
    """class Sphere"""
    def __init__(self, rayon: Number):
        super().__init__(rayon)

def test_sphere():
    """
    """
    s1 =Sphere(100)
    print(s1)

test_sphere()
