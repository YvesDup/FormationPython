



def test(argument):
    """
    """
    print(f'\t{argument = }, {id(argument) = }')

    if isinstance(arg, list):
        argument *= 3
        # for i in range(3):
        #     argument.append('tt')
    else:
        argument =  argument * 3

    return argument


"""
arg = 3 
print(f'{arg = }, {id(arg) = }')
new_arg = test(arg)
print(f'{arg = }, {id(arg) = }')
print(f'{new_arg = }, {id(new_arg) = }')
"""

arg  = [10, 20]
print(f'{arg = }, {id(arg) = }')
new_arg = test(arg)
print(f'{arg = }, {id(arg) = }')
print(f'{new_arg = }, {id(new_arg) = }')
