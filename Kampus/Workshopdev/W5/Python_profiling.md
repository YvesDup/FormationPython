---
marp: true
theme: gaia
paginate: true
_paginate: false
header: ![w:150](img/logo_kampus.png)
footer: (c) yduprat@gmail.com
---
# Formation Python - ![h:100 w:280](img/logo_bnc.png)

Juin/Septembre 2022

_

![h:250](https://www.python.org/static/community_logos/python-logo-generic.svg)

---
<style scoped> {
  font-size: 26px;
}
</style>

# Mesurer les performances

En programmation, il y a 2 domaines sur lesquels peuvent se faire les mesures de performance:

* le temps de traitement
* la mémoire utilisée

ces 2 points peuvent être traités dès la mise en place des tests unitaires et/ou lors des phases de tests d'intégration. Quand ils sont mis en place à ce stade du développement, ils peuvent servir de mesures de référence

---
<style scoped> {
  font-size: 21px;
}
</style>
## Observer le temps de traitement d'une fonction, d'un script

Il existe plusieurs moyens pour mesurer le temps de traitement d'une fonction, d'un script

* faire une mesure locale avec 2 prises de temps entourant la partie de code, directement ou via un décorateur, un context manager

* utiliser des outils plus élaborés comme:
    - la bibliothèque interne [`timeit`](https://docs.python.org/fr/3/library/timeit.html)
    - la bibliothèque interne [`profile / cProfile`](https://docs.python.org/3/library/profile.html)
    - des bibliothèques externes comme:
        + [pyperf](https://pyperf.readthedocs.io/en/latest)
        + [vprof](https://pythonrepo.com/repo/nvdv-vprof-python-monitoring)
        + [line_profiler](https://coderzcolumn.com/tutorials/python/line-profiler-line-by-line-profiling-of-python-code)

**A noter** :

La bibliothèque interne `profile` produit des fichiers d'extension .prof (.cprof) qui peuvent être lus et analysés par la bibliothèque interne `pstats`, ou des outils externes comme **'snakeviz'**.

[Voir ici la mise en oeuvre sous vscode](https://docs.microsoft.com/fr-fr/visualstudio/python/profiling-python-code-in-visual-studio?view=vs-2019)

---
<style scoped> {
  font-size: 26px;
}
</style>
### Observer l'occupation mémoire d'un objet, d'une structure de données

Pour regarder l'occupation mémoire d'un script et des structures de données, il existe plusieurs outils:

* (ne pas) utiliser la fonction interne `sys.getsizeof` 
* utiliser sa propre fonction: voir la fonction `getsize` proposée en Annexe1
* utiliser des bibliothèques externes comme:
    + memory_profiler: <https://pypi.org/project/memory-profiler/>, <https://coderzcolumn.com/tutorials/python/how-to-profile-memory-usage-in-python-using-memory-profiler>
    + pympler: <https://pympler.readthedocs.io/en/latest/>

---
<style scoped> {
  font-size: 22px;
}
</style>
### Annexe1
```python
import sys
from numbers import Number
from collections import deque
from collections.abc import Set, Mapping

ZERO_DEPTH_BASES = (str, bytes, Number, range, bytearray)

def getsize(obj_0):
    """Recursively iterate to sum size of object & members."""
    _seen_ids = set()
    def inner(obj):
        obj_id = id(obj)
        if obj_id in _seen_ids:
            return 0
        _seen_ids.add(obj_id)
        size = sys.getsizeof(obj)
        if isinstance(obj, ZERO_DEPTH_BASES):
            pass # bypass remaining control flow and return
        elif isinstance(obj, (tuple, list, Set, deque)):
            size += sum(inner(i) for i in obj)
        elif isinstance(obj, Mapping) or hasattr(obj, 'items'):
            size += sum(inner(k) + inner(v) for k, v in getattr(obj, 'items')())
        # Check for custom object instances - may subclass above too
        if hasattr(obj, '__dict__'):
            size += inner(vars(obj))
        if hasattr(obj, '__slots__'): # can have __slots__ with __dict__
            size += sum(inner(getattr(obj, s)) for s in obj.__slots__ if hasattr(obj, s))
        return size
    return inner(obj_0)
```