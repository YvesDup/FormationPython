"""module cercle"""
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