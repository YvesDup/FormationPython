import sys

def fizzbuzz(n):
    """Fait bizzfuzz cf exo12
    """
    results = []
    for i in range(1, n+1):
        results.append(i)

    return results

def test_fizzbuzz():
    """fonction de tests pour fizzbuzz
    """
    print(fizzbuzz(0) == [])
    print(fizzbuzz(3) == [1, 2, 'fizz'])
    print(fizzbuzz(5) == [1, 2, 'fizz', 4, 'buzz'])

print(sys.version)
test_fizzbuzz()
