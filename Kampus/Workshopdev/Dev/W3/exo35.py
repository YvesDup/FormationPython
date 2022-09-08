

from typing import Dict

def creer_index(phrase: str) -> Dict[str, int]:
    if not isinstance(phrase, str):
        raise TypeError('"phrase" doit être une string')

    dmots = {}

    for mot in phrase.split():
        if mot in dmots:
            dmots[mot] += 1
        else:
            dmots[mot] = 1

    return dmots

def test_creer_index():
    """test c reer_index"""
    try:
        assert creer_index({}) == {}
    except Exception as e:
        assert isinstance(e, TypeError)
    assert creer_index("") == {}
    assert creer_index("hello") == {'hello':1}
    assert creer_index("hello hello") == {'hello':2}

    print("Done")

test_creer_index()