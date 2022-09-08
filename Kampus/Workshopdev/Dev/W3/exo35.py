"""exo35"""
import collections

from typing import Dict

def creer_index(phrase: str, occurrence: int=1) -> Dict[str, int]:
    """creer l'index des mots d'une phrase"""
    if not isinstance(phrase, str):
        raise TypeError('"phrase" doit être une string')

    dmots = {}
    for mot in phrase.split():
        if mot in dmots:
            dmots[mot] += 1
        else:
            dmots[mot] = 1

    if occurrence > 1:
        # filtrer
        return {k:v for k, v in dmots.items() if v >= occurrence}

    return dmots
def creer_index_counter(phrase: str, occurrence: int=1) -> Dict[str, int]:
    """creer l'index des mots d'une phrase"""
    if not isinstance(phrase, str):
        raise TypeError('"phrase" doit être une string')

    dmots = collections.Counter(phrase.split())
    if occurrence > 1:
        # filtrer
        return {k:v for k, v in dmots.items() if v >= occurrence}

    return dict(dmots)

def creer_index_defaultdict(phrase: str, occurrence: int=1) -> Dict[str, int]:
    """creer l'index des mots d'une phrase"""
    if not isinstance(phrase, str):
        raise TypeError('"phrase" doit être une string')

    dmots = collections.defaultdict(int)
    for mot in phrase.split():
        dmots[mot] += 1

    if occurrence > 1:
        # filtrer
        return {k:v for k, v in dmots.items() if v >= occurrence}

    return dict(dmots)

def test_creer_index():
    """test creer_index"""
    for func in (creer_index, creer_index_defaultdict):
        print(func.__name__)
        # partie 1
        try:
            assert func({}) == {}
        except Exception as e:
            assert isinstance(e, TypeError)
        assert func("") == {}
        assert func("hello") == {'hello':1}
        assert func("hello hello") == {'hello':2}
        assert func("hello hello Bob") == {'hello':2, 'Bob':1}
        s = "ton tonton est ton ami et un ami de ton ami est mon ami"
        d = {'ami': 4, 'ton': 3, 'est': 2, 'de': 1, 'un': 1, 'mon': 1, 'et': 1, 'tonton': 1}
        assert func(s) == d

        # partie 2
        try:
            assert func(s, "") == {}
        except TypeError:
            pass
        except Exception:
            assert False
        assert func(s, 3) == {'ami': 4, 'ton': 3}
        assert func(s, 8) == {}

    print("Done")

test_creer_index()
