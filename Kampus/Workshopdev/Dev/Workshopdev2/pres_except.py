



def pres_except():
    """
    """
    try:
        "1/0"
    except ZeroDivisionError as e:
        print(f'{type(e)} - {str(e)}')
        raise
    except Exception as e:
        print(f'{type(e)} - {str(e)}')
    except BaseException as e:
        print("baseException")
    else:
        print("on passe ici qaud il n'y apas d'erreur")

    finally:
        print("on passe tout le temps la ....")

pres_except()