import sys


def type_simple():
    """Présentation des types simples
    """
    def type_int():
        print("entiers")
        a = 10 # a est un entier
        al = 10_000_000_000_000_000
        print(a)
        print(al)
        b = a
        print(f'{b = }')
        print(f'{id(a) = }, {id(b) = }')
        print('je modifie b'.center(60, '-'))
        b += 10
        print(f'{a = }, {b = }')
        print(f'{id(a) = }, {id(b) = }')

    def type_bool():
        print("booléen")
        bot = True
        bof = False
        print(f'{bot = }, {bof = }')

    def type_float():
        print('flottant')
        f = 0.5
        print(f'{f = }')
        f2 = 1.21e-19
        print(f'{f2 = }')
        print(f'Conversion vers un entier: {int(f) = }')

    def type_cplx():
        print("complexe")
        cplx = 2j + 9
        print(f'{cplx = }, {type(cplx) = }')

    def type_none():
        print("valeur nulle")
        n = None
        print(f'{n = } - {type(None)}')

    def type_string():
        print("string")
        s1 = "hello"
        s2 = 'world !!'
        s3 = """hello
    salut,             yyyyy
    encore"""
        print(f'{s3 = }')
        s4 = s1
        print(f'{s1 = }, {s4 = }')
        print('h' in s1)
        print(s1 == s4)
        print(s1 is s4) # id(s1) == id(4)
        s4 = 'Yves'
        print(f'{s1}, {s4}')
        print(f'{s4[0]=}', f'{s4[len(s4)-1] = }', f'{s4[-1] = }')
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
        x = slice(start, stop, step)
        print(x)
        print(s4[x])
        print(f'{s4.startswith("Yv") = }')
        # s4[2] = 'E'
        s4 = s4.replace('e', 'E')
        print(s4)
        s = 'hello la compagnie'
        print("6 - ", s.count('e'))
        print("7 - ", 'o l' in s)
        print(f'8 - {s = }, {type(s) = }, {isinstance(s, (str)) = }')
        print(f"10 - {s[2:7:2] = }")
        sl = slice(2, 7, 2)
        print(f"10bis - {s[sl] = }")

    type_int()
    type_bool()
    type_float()
    type_cplx()
    type_none()
    type_string()

type_simple()



def type_avance():
    """
    """
    def type_liste():
        # liste
        print('liste')
        l = []
        print(f'{l = }, {type(l) = }')
        l = [10, "vingt", 20.000 , None]
        print(f'{l = }')

        print("modification")
        l.append(False)
        l.insert(2, "Hooper")
        print(f'{l = }')
        print(False in l)
        l.remove(10)
        print(f'{l = }')
        l[2] *=10
        print(f'{l = }')
        l.extend('ABC')
        print(f'{l = }')

        print("parcours de la liste")
        for item in l:
            print(item)
        print("---")

        print("juste les chaines de caractères")
        for item in l:
            if isinstance(item, str):
                print(item)
        print("---")
        print("possible mais moins efficace")
        for i in range(len(l)):
            print(l[i])
        print("---")

        print("Inverser une liste")
        print(l[::-1])

        print("Trier une liste")
        l1 = [10, 0, -5, True, 2.89, -1.2e-19]
        print(l1)
        l1.sort()
        print(l1)

        print("extend".center(60))
        s = "hello"
        # l1.extend(s) # l += s
        print(l1)
        l1.append(l)
        print("------", id(l), id(l1[-1]))
        print(l1)
        l.remove(None) # l1[-1].remove(None)
        l.remove(20.0) # l1[-1].remove(20.0)
        print(l1)

        # copy
        print("copy")
        import copy
        lc = copy.copy(l1) # copy.deepcopy() copie profonde
        print(f'{id(l1) = } , {id(lc) = }')
        print(f'{id(l1[-1]) = } , {id(lc[-1]) = }')
        lc = copy.deepcopy(l1) # copy.deepcopy() copie profonde
        print(f'DC {id(l1) = } , {id(lc) = }')
        print(f'DC {id(l1[-1]) = } , {id(lc[-1]) = }')

    # ensemble
    def type_set():
        s1 = {10, 20, 40}
        print(f'{s1=}')
        s2 = {20, 30, 60, 60}
        # print(f'{s2=}')
        s1.add(80)
        print(f'{s1=}')
        print(80 in s1)
        # print(s1[1])
        s1.add(10)
        print(f'{s1=}')
        for item in s1:
            print(item)

        s1.remove(80)
        # print(f'{s1=}')

        #operation ensembliste
        print(f'{s1=}')
        print(f'{s2=}')
        print(f'{s1 & s2 = }')
        print(f'{s1 | s2 = }')
        print(f'{s1 ^ s2 = }')
        print(f'{s1 - s2 = }')
        print(f'{s2 - s1 = }')
        print({10, 20}.issubset(s1))
        print({100, 25}.isdisjoint(s1))
        print({10, 20, 40, 50}.issuperset(s1))

        l = [10, 20, 30, 10, 20, 40, 10, 0, 0, 0]
        print(l)
        l = list(set(l))
        print(l)
        # un set vide
        sss = set()
    def type_dict():
        # dictionnaire
        d = {} # dictionnaire 
        d = { "1": 10, "2": [10, 20] , 4: "quatre" }
        print(f'{d = }')
        print(f'{4 in d = }')
        print(f'{d[4] = }')
        d[4] = 4
        print(f'{d[4] = }')
        print(f'{d.get(5, "Pas de key") = }')
        print(d.keys())
        print(d.values())
        print(d.items())
        print("___"*20)
        for k in d:  # d.keys(): 
            print(k, '->', d[k])

        print("___"*20)
        for item in d.items():
            print(item[0], '->', item[1])
        print("___"*20)
        for k, v in d.items():
            print(k, '->', v)

        del d["2"]
        v = d.pop(4)
        print(v)

        print(d)
        dd = { 5:"cinq", '1':["un", "I", 1], True:"VRAI !!"}
        d.update(dd) 
        print(d)

    def type_tuple():
        """
        """

    type_liste()
#    type_set()
#    type_dict()
#    type_tuple()

# type_avance()