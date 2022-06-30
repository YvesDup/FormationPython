import sys

def fizzbuzz(n):
    """Fait bizzfuzz cf exo12
    """
    results = []
    for i in range(1, n+1):
        if i % 15 == 0:
            results.append('fizzbuzz')
        elif i % 3 == 0:
            results.append('fizz')
        elif i % 5 == 0:
            results.append('buzz')
        else:
            results.append(i)

    return results

def test_fizzbuzz():
    """fonction de tests pour fizzbuzz
    """
    print(fizzbuzz(0) == [])
    print(fizzbuzz(3) == [1, 2, 'fizz'])
    print(fizzbuzz(5) == [1, 2, 'fizz', 4, 'buzz'])
    print(fizzbuzz(1000).count('fizzbuzz') == 1000//15)

print(sys.version)
test_fizzbuzz()
