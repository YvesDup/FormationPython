class A:
    pass

print(dir(A))

print(A.__mro__)
print(A.__bases__)


class B(A):
    def __init__(self, *args):
        self.toto = 10

class C(B):
    pass

print(C.__mro__)
print(C.__bases__)

print(C.toto)
