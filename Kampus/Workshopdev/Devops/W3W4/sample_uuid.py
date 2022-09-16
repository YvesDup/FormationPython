import sys
import uuid

x = str(uuid.uuid4())
print(x)

class Obj:

    """ """
    def __init__(self, name, val):
        """ """
        self._name = name
        self._val = val

    def get_name(self) -> str:
        """ ohoh"""
        return self._name # appel à un attribut privé pour une méthode publique

o = Obj('Yves', 57)
print(f"{o._name = } et {o.get_name() = }")





class ObjUUid(Obj):
    """"""
    def __init__(self, name, val):
        """bolobolo"""
        super().__init__(self, name, val)
        self.__uuid = str(uuid.uuid4())

    def get_uuid(self) -> str:
        """bolobolo"""
        return self.__uuid

o = ObjUUid('Yves', 57)
print(f"{o._name = } et {o.get_name() = }")
try:
    print(f'{o.get_uuid() = }')
    print(f'{o.__uuid = }')
except Exception as e:
    print(e)
