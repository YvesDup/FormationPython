

from typing import Dict

def creer_index(phrase: str, occurrence: int=1) -> Dict[str, int]:
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
        return { k:v for k, v in dmots.items() if v >= occurrence}

    return dmots

def test_creer_index():
    """test creer_index"""
    # partie 1
    try:
        assert creer_index({}) == {}
    except Exception as e:
        assert isinstance(e, TypeError)
    assert creer_index("") == {}
    assert creer_index("hello") == {'hello':1}
    assert creer_index("hello hello") == {'hello':2}
    assert creer_index("hello hello Bob") == {'hello':2, 'Bob':1}
    s = "ton tonton est ton ami et un ami de ton ami est mon ami"
    d = {'ami': 4, 'ton': 3, 'est': 2, 'de': 1, 'un': 1, 'mon': 1, 'et': 1, 'tonton': 1}
    assert creer_index(s) == d

    # partie 2
    assert creer_index(s, 3) == {'ami': 4, 'ton': 3}

    print("Done")

test_creer_index()