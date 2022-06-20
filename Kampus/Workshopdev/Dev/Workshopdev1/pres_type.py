import sys


def type_simple():
    """Présentation des types simples
    """
    print("entiers")
    a = 10 # a est un entier
    al = 10_000_000_000_000_000
    print(a)
    print(al)
    b = a 
    print(f'{b = }')
    print(f'{id(a) = }, {id(b) =}')
    print('je modifie b'.center(60, '-'))
    b += 10
    print(f'{b = }')
    print(f'{id(a) = }, {id(b) =}')
    print('flottant')
    f = 0.5 
    print(f'{f=}')
    fl = f 
    print("booléen")
    bot = True
    bof = False
    print(f'{bot = }, {bof = }')
    print("complexe")
    cplx = 2j + 9
    print(cplx)
    print("valeur nulle")
    n = None
    print(f'{n = } - {type(None)}')
    print("string")
    s1 = "hello"
    s2 = 'world !!'
    s3 = """hello
salut,             yyyyy
encore"""
    print(s3)
    s4 = s1
    print(f'{s1}, {s4}')
    print('h' in s1)
    print(s1 == s4)
    print(s1 is s4)

type_simple()