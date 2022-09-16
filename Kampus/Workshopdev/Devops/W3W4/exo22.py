import sys

import exo20

class Losange(exo20.Parallelo):

    def __init__(self, cote, angle):
        super().__init__(cote, cote, angle)
        # exo20.Parallelo.__init__self, *args)

    # conversion en string
    def __str__(self) -> str:
        return f"LOSANGE {self.p_cote}, {self.angle}"

    def __repr__(self) -> str:
        return self.__str__()

def test_losange():
    """Losange Test"""
    l = Losange(50, 65)
    print(l)

    ll = [l, exo20.Parallelo(20, 30, 75)]
    print(ll)

class Carre(exo20.Parallelo):
    """class Carre herits from Parallelo"""

    def __init__(self, p_cote, g_cote):
        super().__init__(p_cote, g_cote, 90)
        # exo20.Parallelo.__init__self, *args)

    # conversion en string
    def __str__(self) -> str:
        return f"CARRE {self.p_cote}, {self.g_cote}"

    def __repr__(self) -> str:
        return self.__str__()
if __name__ == "__main__":
    print(sys.version)
    test_losange() 
