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

# isinstance(10, (int, float))
def test_carre():
    """
    """
    for cls in (Carre0, Carre1, Carre2):
        try:
            c = cls(30)
            print(c, f'{cls.__mro__ = }, {cls.__bases__ = }')
            print(vars(c), c.__dict__)
        except Exception as e:
            print(f'class {cls.__name__!a} -> {e}')

test_carre()