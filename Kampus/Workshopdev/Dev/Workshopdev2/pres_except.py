



def pres_except():
    """
    """
    try:
        1/0
    except:
        pass
    except:
        pass

    else:
        print("on passe ici qaud il n'y apas d'erreur")

    finally:
        print("on passe tout le temps la ....")