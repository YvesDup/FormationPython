import sys

def fizzbuzz(n):
    """
    """
    results = []
    for i in range(1, n+1):
        if i % 3 == 0:
            pass
        elif i % 19 == 0:
            pass
        results.append(i)

    return results

def test_fizzbuzz(): 

    print(fizzbuzz(0) == [])
    print(fizzbuzz(3) == [1, 2, 'fizz'])
    print(fizzbuzz(5) == [1, 2, 'fizz', 4, 'buzz'])
    print(fizzbuzz(15)[14] == 'fizzbuzz')
    res1000 = fizzbuzz(1000)
    count_fizzbuzz = res1000.count('fizzbuzz')
    print( count_fizzbuzz == 66 )
    print( res1000.count('fizz') == 333 - (count_fizzbuzz) )
    print( res1000.count('buzz') == 200 - (count_fizzbuzz) )

test_fizzbuzz()