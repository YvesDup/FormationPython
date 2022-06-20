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
    print(s1 is s4) # id(s1) == id(4)
    s4 = 'Yves'
    print(f'{s1}, {s4}')
    print(f'{s4[0]=}', f'{s4[len(s4)-1] = }', f'{s4[-1] = }')
    # print(s4[10])
    print(s4[-len(s4)])
    print("slicing")
    start = 0
    stop = len(s4) # borne haute exclue quant à sa valeur
    step = 1  # pas
    print(s4[start:stop:step])
    step = 3  # pas
    print(s4[start:stop:step])
    print(s4[0:2])
    print(s4[2:None])
    print(s4[1:3])
    print(s4[::-1])
    print(s4[-2:])

type_simple()