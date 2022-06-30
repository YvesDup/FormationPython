


def analyse_texte(val, *args):
    """
    """
    args += (val, )
    for arg in args:
        if isinstance(arg, str):
            pass


    return "", "", 0.0

def test_analyse_texte():
    """
    """
    tests = (
        (), 
        ()
    )

    print(analyse_texte('hello', 2.234, 't') == ('t', 'hello', 3.0))

test_analyse_texte()
