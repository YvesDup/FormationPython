import math
import sys
from typing import Union, List, Set, Tuple

def racine_carre(val: Union[float, int]) -> float:
    """calcul de la racine carrée"""
    return math.sqrt(val)

def main():
    print(racine_carre(10))
    print(racine_carre(10.169))
    # print(racine_carre("10"))


Number = Union[float, int] # alias
def minmax(serie: Union[List, Set, Tuple]) -> Tuple[Number, Number]:
    """Renvoie le min et le max à partir d'une serie de chiffres"""
    return min(serie), max(serie)

if __name__ == '__main__':
    main()
    print(minmax.__name__, '->', minmax.__annotations__, minmax.__doc__)