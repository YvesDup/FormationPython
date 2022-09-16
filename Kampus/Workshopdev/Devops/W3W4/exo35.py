def creer_index(phrase: str, occurrence_mini: int=1) -> dict:
    """
    """
    d = {}
    for mot in phrase.split():
        pass

    if occurrence_mini > 1:
        return {k: v for k, v in d.items() if v > occurrence_mini}

    return d

def test_creer_index():
    """
    """

    assert creer_index("") == {}
    print("all tests done !!!")

if __name__ == '__main__':
    test_creer_index()