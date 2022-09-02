class A:
    pass

print(dir(A))

print(A.__mro__)
print(A.__bases__)


class B(A):
    pass

class C(B):
    pass

print(C.__mro__)
print(C.__bases__)

print(C.toto)
