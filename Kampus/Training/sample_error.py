import sys

# import matplotlib

def test(diviseur=0):
    try:
        1/diviseur
    except ZeroDivisionError:
        print('zero division error')
    except TypeError:
        print('autre error')
        raise
    except Exception:
        print("tout ce qui passe ....")
    else:
        print('no error')

def main():
    test(0)
    test(10)
    test('10')

if __name__ == '__main__':
    main()