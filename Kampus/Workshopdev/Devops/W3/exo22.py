import exo20

class Losange(exo20.Parallelo):

    def __init__(self, *args):
        super().__init__(*args)
        # exo20.Parallelo.__init__self, *args)

def test_losange():
    """Losange Test"""
    l = Losange()
    print(l)

if __name__ == "__main__":
    print(sys.version)
    test_losange() 
