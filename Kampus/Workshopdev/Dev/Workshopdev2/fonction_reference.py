



def test(argument):
    """
    """
    print(f'\t{argument = }, {id(argument) = }')

    argument *= 3

    return argument


for arg in (3, [10, 20], "chaine"):
    print('---'*20)
    print(f'{arg = }, {id(arg) = }')
    new_arg = test(arg)
    print(f'{arg = }, {id(arg) = }')
    print(f'{new_arg = }, {id(new_arg) = }')
