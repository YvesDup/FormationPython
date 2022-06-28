

def fizzbuzz(n):
    """
    """
    results = []
    for value in range(1, n+1):
        print(value)

    return results

def test_fizzbuzz():
    """
    """
    assert fizzbuzz(0) ==  []
    assert fizzbuzz(3) ==  [1, 2, "fizz"]

test_fizzbuzz()