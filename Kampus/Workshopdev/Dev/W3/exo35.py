

from typing import Dict

def creer_index(phrase: str) -> Dict[str, int]:
    d = {}

    for mot in phrase.split():
        pass

    return d

def test_creer_index():
    """test c reer_index"""
    assert creer_index("") == {}
    assert creer_index("hello") == {'hello':1}
    print("Done")

test_creer_index()