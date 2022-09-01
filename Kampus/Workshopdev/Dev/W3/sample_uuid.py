import sys
import uuid

x = str(uuid.uuid4())
print(x)

class Obj:
  def __init__(self, name, val):
    self._name = name
    self._val = val 

  def get_name(self) -> str:
    return self._name # appel à un attribut privé pour une méthode publique

o = Obj('Yves', 57)
print(f"{o._name = } et {o.get_name() = }")
try:
    print(o.__uuid)
except:
    ...
print(sys.path)