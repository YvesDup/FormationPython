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

    def carre(self):
        return self.val ** 2

try:
    t = Test() # ne fonctionne pas car un paramètre positionnel
except Exception as e:
    print(type(e), str(e))

t = Test(10)
print(f'{t = }, {t.val =}')

print(f"{t.carre() = } vs {Test.carre(t) = }")
print(t.records)
print(vars(t))
try:
    t.essai_ajout = 10
    print(t.essai_ajout)
except Exception as e:
    print(e)