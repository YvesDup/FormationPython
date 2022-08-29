import math
import sys
from typing import Union

def racine_carre(val: Union[float, int]):
    return math.sqrt(val)

def main():
    print(racine_carre(10))
    print(racine_carre(10.169))
    print(racine_carre("10"))

if __name__ == '__main__':
    main()