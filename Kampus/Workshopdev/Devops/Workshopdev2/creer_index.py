import os
import sys


def creer_index(mots, min_occurence=1, debug=True):
    """
    """
    dmots = {}
    # key c'est le mot
    # value est le nombre de fois ou le mot apparait
    for mot in mots.split():
        if mot in dmots:
            dmots[mot] += 1
        else:
            dmots[mot] = 1
        if debug:
            print(f' {mot = } -> {dmots[mot] = }')

    # filter
    if min_occurence > 1:
        dd = {}
        for k, v in dmots.items():
            if v >= min_occurence:
                dd[k] = v
        dmots = dd

    return dmots

def test_creer_index():
    """
    """
    print(creer_index("") == {})
    print(creer_index("toto") == {"toto":1})
    print(creer_index("toto toto") == {"toto":2})
    print(creer_index("toto toto", 3) == {})

print(sys.version)
print(os.getcwd())
test_creer_index()