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
print(f"{t.__super_private = }")