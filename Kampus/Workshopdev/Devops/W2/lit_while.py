

def lit_tantque():
    """
    """
    while True:
        valeur_tapee = input("tapez qlqchose:")
        print(f'{valeur_tapee = }')

def lit_tantque_1():
    """
    """
    valeur_tapee = ""
    while valeur_tapee != "QQ":
        valeur_tapee = input("tapez qlqchose:")
        print(f'{valeur_tapee = }')

def lit_tantque_2():
    """
    """
    while True:
        valeur_tapee = input("tapez qlqchose:")
        if valeur_tapee == "QQ":
            break
        print(f'{valeur_tapee = }')
        
def lit_tantque_2():
    """
    """
    while input("tapez qlqchose:") != "QQ":
        pass
        # print(f'{valeur_tapee = }')

lit_tantque()
