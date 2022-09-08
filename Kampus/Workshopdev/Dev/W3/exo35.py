

from typing import Dict

def creer_index(phrase: str) -> Dict[str, int]:
    if not isinstance(phrase, str):
        raise TypeError('"phrase" doit être une string')

    d = {}

    for mot in phrase.split():
        pass

    return d

def test_creer_index():
    """test c reer_index"""
    try:
        assert creer_index({}) == {}
    except Exception as e:
        assert isinstance(e, TypeError) 
    assert creer_index("") == {}
    assert creer_index("hello") == {'hello':1}
    print("Done")

test_creer_index()