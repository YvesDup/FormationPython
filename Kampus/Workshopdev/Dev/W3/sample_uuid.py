import sys
import uuid

x = str(uuid.uuid4())
print(x)

class Obj:
  def __init__(self, name, val):
    self._name = name
    self._val = val
    self.__uuid = str(uuid.uuid4())

  def get_name(self) -> str:
    return self._name # appel à un attribut privé pour une méthode publique

  def get_uuid(self):
    return self.__uuid 

o = Obj('Yves', 57)
print(f"{o._name = } et {o.get_name() = }")
try:
    print(f'{o.get_uuid() = }')
    print(f'{o.__uuid = }')
except Exception as e:
    print(e)
