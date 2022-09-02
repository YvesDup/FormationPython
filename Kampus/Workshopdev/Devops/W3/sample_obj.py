
def class_obj():
    class Obj:
        pass

    o1 = Obj()
    print(f'{o1 = }')
    o2 = o1 
    print(f'{o1 is o2 =}')

    l = [o1]
    l.append(o2)
    print(l, o1 in l)

class Test:
    """Ma premiere classe """
    def __init__(self, val):
        """init"""
        self.val = val

    def calcul_moyenne(self) -> float:
        """ma premiere methode"""
        return self.val ** 3

try:
    t = Test() # ne fonctionne pas car un paramètre positionnel
except Exception as e:
    print(e)

    try:
    t = Test(10, 20) # ne fonctionne pas car 2 paramètres positionnels
except Exception as e:
    print(e)

t = Test(10)
print(f'{t = } - {t.val = }')
print('moyenne = ', t.calcul_moyenne())
print('moyenne = ', Test.calcul_moyenne(t))
