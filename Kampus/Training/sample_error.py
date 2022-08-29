import sys

def test():
    try: 
        1/0
    except ZeroDivisionError:
        print('zero deivision error')
    except ValueError:
        print('autre')
    else:
        print('no error')

def main():
    test()

if __name__ == '__main__':
    main()