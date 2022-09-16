"""La sphere"""
import math

import class_cercle as cc # cc est un alias

class Sphere(cc.Cercle):
    """class Sphere"""
    def __init__(self, rayon: cc.Number):
        print(vars(self))
        super().__init__(rayon)
        print(vars(self))
        self._bidon = None
        print(vars(self))

    def surface(self) -> float:
        return 4 * self._rayon**2 * math.pi

def test_sphere():
    """rrr
    """
    s1 =Sphere(100)
    print(s1)
    print(f'{s1.perimetre() = } - {s1.surface() = } / {cc.Cercle.surface(s1) = }')
    l1 = [cc.Cercle(5), s1, cc.Cercle(8)]
    print(l1)
    l1.sort(reverse=True)
    print(l1)

print('+++'*20)
print(f'name: {__name__!a} from {__file__!a}')
print('+++'*20)

if __name__ == '__main__':
    test_sphere()
