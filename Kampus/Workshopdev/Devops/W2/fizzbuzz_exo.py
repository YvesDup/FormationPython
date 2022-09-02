import sys

def fizzbuzz(n):
    """n est un parametre formel
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

    x = 0
    # x est iun parametre effectif
    print(fizzbuzz(x) == [])
    print(fizzbuzz(3) == [1, 2, 'fizz'])
    print(fizzbuzz(5) == [1, 2, 'fizz', 4, 'buzz'])
    print(fizzbuzz(15)[14] == 'fizzbuzz')
    res1000 = fizzbuzz(1000)
    count_fizzbuzz = res1000.count('fizzbuzz')
    print( count_fizzbuzz == 66 )
    print( res1000.count('fizz') == 333 - (count_fizzbuzz) )
    print( res1000.count('buzz') == 200 - (count_fizzbuzz) )

test_fizzbuzz()
