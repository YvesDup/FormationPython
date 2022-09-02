
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

    def __init__(self, val):
        self.val = val

try:
    t = Test() # ne fonctionne pas car un paramètre positionnel
except Exception as e:
    print(e)
t = Test(10)
print(t)