



def test(argument):
    """
    """
    print(f'\t{argument = }, {id(argument) = }')

    argument =  argument * 3

    return argument



arg = 3 
print(f'{arg = }, {id(arg) = }')
new_arg = test(arg)
print(f'{arg = }, {id(arg) = }')
print(f'{new_arg = }, {id(new_arg) = }')
