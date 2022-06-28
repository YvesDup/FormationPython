import sys

def analyse_texte(*args):
    """
    """
    pluscourte_chaine = ""
    pluslongue_chaine = ""
    moyenne_longueur = 0.0
    nb_chaines = 0
    lg_total = 0
    lg_max = -1
    lg_min = sys.maxsize 

    for arg in args:
        if isinstance(arg, str):
            lg = len(arg)
            lg_total += lg
            nb_chaines += 1

            if lg < lg_min:
                lg_min = lg
                pluscourte_chaine = arg
            if lg > lg_max:
                lg_max = lg
                pluslongue_chaine = arg

    if nb_chaines:
        moyenne_longueur = lg_total / nb_chaines

    return pluscourte_chaine, pluslongue_chaine, moyenne_longueur

def test_analyse_texte():
    """
    """
    print(analyse_texte('hello', 2.234, 't'))
    assert analyse_texte('hello', 2.234, 't') == ('t', 'hello', 3.0)

print(sys.version)
test_analyse_texte()



def analyse_texte_v2(*args):
    """
    """
    l = list(filter(lambda x: isinstance(x, str), args))
    min_str = min(l, key=len)
    max_str = max(l, key=len)
    stralls = ''.join(l)

    return min_str, max_str, len(stralls) / len(l)

