"""module cercle"""
import math
from typing import Union

Number = Union[float, int] # en 3.10 float | int

class Cercle:
    """class Cercle"""
    def __init__(self, rayon: Number):
        self._rayon = rayon

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {self._rayon:.03f}"

    def __repr__(self) -> str:
        return f"<{self.__str__()}>"

    def perimetre(self) -> float:
        """xxx"""
        return 2 * self._rayon * math.pi

    def surface(self) -> float:
        """yyy"""
        return (self._rayon ** 2) * math.pi

    # operator de comparaison
    def __lt__(self, other: Union["Cercle", int, float]) -> bool:
        if isinstance(other, Cercle):
            return self._rayon < other._rayon
        elif isinstance(other, (int, float)):
            return self._rayon < other
        raise TypeError("other must a Cercle, an int or a float")

def test_cercle():
    """Test un cercle
    """
    c1 = Cercle(10)
    print(f'{c1!s} - {c1!r}')
    print(f'{c1.perimetre() = } - {c1.surface() = }')
    l1 = [c1, Cercle(5), Cercle(8)]
    print(f'{c1 < Cercle(30) = }')
    print(f'{c1 < 1 = }')
    try:
        print(f'{1 < c1 = }')
    except TypeError as e:
        print(e)

    print(l1)
    l1.sort()
    print(l1)


test_cercle()
