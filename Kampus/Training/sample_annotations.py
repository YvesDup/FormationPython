import math
import sys

def racine_carre(val):
    return math.sqrt(val)

def main():
    print(racine_carre(10))
    print(racine_carre(10.169))
    print(racine_carre("10"))

if __name__ == '__main__':
    main()