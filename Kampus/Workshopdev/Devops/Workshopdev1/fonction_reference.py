



def test(argument):
    """
    """
    print(f'\t{argument = }, {id(argument) = }')

    argument =  argument * 3

    return argument



arg = 3 
print(f'{arg = }, {id(arg) = }')
test(arg)
print(f'{arg = }, {id(arg) = }')
