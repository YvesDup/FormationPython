import sys

def fizzbuzz(n):
    """
    """
    results = []
    for i in range(1, n+1):
        # print(i)
        results.append(i)

    return results

def test_fizzbuzz(): 

    print(fizzbuzz(0) == [])
    print(fizzbuzz(3) == [1, 2, 'fizz'])
    print(fizzbuzz(5) == [1, 2, 'fizz', 4, 'buzz'])
    print(fizzbuzz(15)[14] == 'fizzbuzz')

test_fizzbuzz()