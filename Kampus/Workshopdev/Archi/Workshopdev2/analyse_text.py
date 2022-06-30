import sys

def analyse_texte(val, *args):
    """
    """
    lg_min = sys.maxsize
    lg_max = 0
    long_mot = ''
    court_mot = ''
    lg_total = 0
    nb_mots = 0
    args = (val,) + args # pour respecter l'ordre
    for arg in args:
        if isinstance(arg, str):
            lg = len(arg)
            if lg < lg_min:
                court_mot = arg
                lg_min = lg
            if lg > lg_max:
                long_mot = arg
                lg_max = lg
            nb_mots += 1
            lg_total += lg

    if nb_mots:
        return court_mot, long_mot, lg_total/nb_mots

    raise ValueError("Pas de string :-(")

def test_analyse_texte():
    """
    """
    tests = (
        (), 
        ()
    )

    print(analyse_texte('hello', 2.234, 't') == ('t', 'hello', 3.0))

test_analyse_texte()

def analyse_texte_v2(val, *args):
    args = (val,) + args # pour respecter l'ordre
    mots = tuple(map(lambda x: isinstance(x, str), args))
    if mots:
        court_mot = min(mots, key=len)
        long_mot = max(mots, key=len)
        moyenne = "".join(mots) / len(mots)
        return court_mot, long_mot, moyenne

    raise ValueError("pas de string :-(")
