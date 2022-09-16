import exo20
import exo22

class Carre0(exo20.Parallelo):
    def __init__(self, cote):
        """"""
        super().__init__(cote, cote, 90)

class Carre1(exo22.Losange):
    def __init__(self, cote):
        """"""
        exo22.Losange.__init__(self, cote, 90)

class Carre2(exo22.Rectangle):
    def __init__(self, cote):
        """"""
        super().__init__(cote, cote)

def test_carre():
    """
    """
    ...

test_carre()