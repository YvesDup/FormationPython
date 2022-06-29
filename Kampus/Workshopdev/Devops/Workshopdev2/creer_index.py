import os
import sys


def creer_index(mots, min_occurence=1, debug=True):
    """
    """
    dmots = {}
    # key c'est le mot
    # value est le nombre de fois ou le pot apparait
    for mot in mots.split():
        if mot in dmots:
            dmots[mot] += 1
        else:
            dmots[mot] = 1
        if debug:
            print(f' {mot = } -> {dmots[mot] = }')

    return dmots

def test_creer_index():
    """
    """
    print(creer_index("") == {})
    print(creer_index("toto") == {"toto":1})
    print(creer_index("toto toto") == {"toto":2})

print(sys.version)
print(os.getcwd())
test_creer_index()