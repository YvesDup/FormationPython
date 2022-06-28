

def fizzbuzz(n):
    """
    """
    results = []
    for value in range(1, n+1):
        if value % 5 == 0 and value % 3 == 0:
        # if value % 15 == 0:
            results.append('fizzbuzz')
        elif value % 5 == 0:
            results.append('buzz')
        elif value % 3 == 0:
            results.append('fizz')
        else:
            results.append(value)

    return results

def test_fizzbuzz():
    """
    """
    assert fizzbuzz(0) ==  []
    print(fizzbuzz(3))
    assert fizzbuzz(3) ==  [1, 2, "fizz"]
    assert fizzbuzz(1000).count('fizzbuzz') == 1000//15

test_fizzbuzz()