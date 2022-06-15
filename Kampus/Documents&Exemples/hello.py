import sys

if len(sys.argv) > 2:
    print(f'hello -{sys.argv[1]}-')
else:
    print('Hello inconnu')
