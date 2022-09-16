class A:
    pass

print(dir(A))
print(A.__mro__)
print(A.__class__.__name__)

class A:
    pass
class B(A): # j'hérite de A
    pass
class C(B): # j'hérite de B
    pass

class D: # j'hérite de B
    pass

class E(C, D):
    pass

print(B.__mro__)
# renvoie un tuple qui contient toutes les classes héritées
# directement ou via les classes héritées intermédiaires
# ('<class B>', '<class A>', '<class object>')

print(C.__bases__)
# Renvoie un tuple qui contient les classes parentes
# ('class B',)

print(E.__bases__)