import collections

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
    """
    """
    d = collections.Counter(phrase.split())

    if occurrence_mini > 1:
        return {k: v for k, v in d.items() if v >= occurrence_mini}

    return d

def test_creer_index():
    """
    """

    assert creer_index("") == {}
    assert creer_index("hello") == {"hello": 1}
    assert creer_index("hello bye") == {"hello": 1, "bye": 1}
    assert creer_index("hello hello") == {"hello": 2}
    assert creer_index("", 10) == {}
    s = "ton tonton est ton ami et un ami de ton ami est mon ami"
    d1 = {'ami': 4, 'ton': 3, 'est': 2, 'de': 1, 'un': 1, 'mon': 1, 'et': 1, 'tonton': 1}
    d2  ={'ami': 4, 'ton': 3}
    for func in (creer_index, creer_index1):
        print(func.__name__.center(60, '.'))
        assert func(s) == d1
        assert func(s, 3) == d2


    print("all tests done !!!")

if __name__ == '__main__':
    test_creer_index()