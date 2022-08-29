import sys

def test(diviseur=0):
    try: 
        1/diviseur
    except ZeroDivisionError:
        print('zero division error')
    except ValueError:
        print('autre')
    else:
        print('no error')

def main():
    test()

if __name__ == '__main__':
    main()