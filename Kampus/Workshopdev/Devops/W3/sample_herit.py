class A:
    pass

print(dir(A))

print(A.__mro__)
print(A.__bases__)


class B(A):
    def __init__(self, *args, **kwargs):
        self.toto = 10

class C(B):
    pass

print(C.__mro__)
print(C.__bases__)

c = C()
print(c.toto)
