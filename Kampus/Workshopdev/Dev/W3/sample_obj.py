""" Presntation des objets en python"""

def show_obj():
    class Obj:
        """Presentation d'un objet simple"""
        # pass

    o = Obj()
    print(o)

    o2 = Obj()
    print(o == o2)

class Test:
    """Classe avec arametre"""
    def __init__(self, val):
        self.val = val
        self.test = False
        self.records = {}
        self._private = 10
        self.__super_private = None 

    def carre(self):
        return self.val ** 2

    def show_super_private(self):
        return self.__super_private

    def __str__(self) -> str:
        return f"[{self.__class__.__name__}:val={self.val}]"

    def __repr__(self) -> str:
        return self.__str__().upper()

try:
    t = Test() # ne fonctionne pas car un paramètre positionnel
except Exception as e:
    print(type(e), str(e))

t = Test(10)
print(f'{t}, {t.val =}')
l = [t, t]
print(l)

print(f"{t.carre() = } vs {Test.carre(t) = }")
print(t.records)
print(vars(t))
try:
    t.essai_ajout = 10
    print(t.essai_ajout)
except Exception as e:
    print(e)
else:
    print(vars(t))

del t.val
print(vars(t))
print(f"{t._private = }")
print(t.show_super_private()) 
try:
    print(f"{t.__super_private = }")
except Exception as e:
    print(e)

import math
from typing import Union

Number = Union[float, int]

class Cercle:
    """class Cercle"""
    def __init__(self, rayon: Number):
        self._rayon = rayon

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {self._rayon:.03f}"

    def __repr__(self) -> str:
        return f"<{self.__str__()}>"

    def perimetre(self) -> Number:
        return 2 * self._rayon * math.pi

    def surface(self) -> Number:
        return (self._rayon ** 2) * math.pi

def test_cercle():
    """Test un cercle
    """
    c1 = Cercle(10)
    print(f'{c1!s} - {c1!r}')
    print(f'{c1.perimetre() = } - {c1.surface() = }')
test_cercle()