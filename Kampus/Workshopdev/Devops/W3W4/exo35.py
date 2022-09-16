def creer_index(phrase: str, occurrence_mini: int=1) -> dict:
    """
    """
    d = {}
    for mot in phrase.split():
        if mot in d:
            d[mot] += 1
        else:
            d[mot] = 1

    if occurrence_mini > 1:
        return {k: v for k, v in d.items() if v >= occurrence_mini}

    return d

def creer_index1(phrase: str, occurrence_mini: int=1) -> dict:
    """
    """

    pass
def test_creer_index():
    """
    """

    assert creer_index("") == {}
    assert creer_index("hello") == {"hello": 1}
    assert creer_index("hello bye") == {"hello": 1, "bye": 1}
    assert creer_index("hello hello") == {"hello": 2}
    assert creer_index("", 10) == {}
    print("all tests done !!!")

if __name__ == '__main__':
    test_creer_index()